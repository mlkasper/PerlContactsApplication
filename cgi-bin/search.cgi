#!/usr/bin/perl -w

use strict; 
use warnings; 
use DBI; 
use CGI qw(:standard); 

my $dsn = "DBI:mysql:mikasper"; 
my $username = "root"; 
my $password = "password"; 

my %attr = (PrintError =>0, RaiseError=>1); 
my $dbh = DBI->connect($dsn, $username, $password, \%attr);

my $option = param('lname'); 


 print "Content-type: text/html\n\n";
 print "<html>\n<head>\n <title>Search Results</title>\n</head>\n<body>\n";
 my $sql = "select id, lname, fname, phone, email from contacts where lname='$option'";
my $sth = $dbh->prepare($sql);
$sth->execute;
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
while (my @row = $sth->fetchrow_array) {
	print "<tr><td align='center'>$row[0]</td>
	<td align='center'>$row[2] $row[1]</td>
	<td align='center'>$row[3]</td>
	<td align='center'>$row[4]</td>
	</tr>\n";
}
print "</table></center>\n";
print "<br><br><br><center><form><input type='button' value='Back' onclick='history.back()'></form></center>";

print "</body></html>\n";
