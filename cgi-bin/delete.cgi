#!/usr/bin/perl

use strict;
use warnings;
use DBI;
use CGI qw(:standard);

my $dsn = "DBI:mysql:USERNAME";
my $username = "root";
my $password = "PASSWORD";

my %attr = (PrintError =>0, RaiseError=>1);
my $dbh = DBI->connect($dsn, $username, $password, \%attr);

my $id = param('uid'); 

my $sql = "DELETE FROM contacts where id = '$id'"; 
my $sth = $dbh->prepare($sql); 
$sth->execute;

my $newsql = q/SELECT id, lname, fname, phone, email from contacts/; 
my $newsth = $dbh->prepare($newsql);
$newsth->execute;  
 print "Content-type: text/html\n\n";
 print "<html>\n<head>\n <title>Contact Removed</title>\n</head>\n<body>\n";
print '<center><h2>All Contacts</h2></center>';
print '<center><table border="1" width="800px">';

#Print Header Names
print "
<tr>
<th>ID</th>
<th>Name</th>
<th>Phone</th>
<th>Email</th>
</tr>";
#prints all the rows and assigns them a html table
while (my @row = $newsth->fetchrow_array) {
        print "<tr><td align='center'>$row[0]</td>
        <td align='center'>$row[2] $row[1]</td>
        <td align='center'>$row[3]</td>
        <td align='center'>$row[4]</td>
        </tr>\n";
}
print "</table></center>\n";
print "<br><br><br><center><form><input type='button' value='Back' onclick='window.history.go(-2)'></form></center>";
print "</body></html>\n";
$dbh->disconnect();
