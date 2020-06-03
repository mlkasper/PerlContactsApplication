#!/usr/bin/perl -w

use strict; 
use warnings; 
use DBI; 
use CGI qw(:standard); 

my $q = new CGI; 
my $dsn = "DBI:mysql:USERNAME"; 
my $username = "root"; 
my $password = "PASSWORD"; 

my $q = new CGI; 

my %attr = (PrintError =>0, RaiseError=>1); 
my $dbh = DBI->connect($dsn, $username, $password, \%attr); 

my $userid = $q->param('id'); 
my $userlname = $q->param('lname'); 
my $userfname = $q->param('fname'); 
my $usernum = $q->param('number'); 
my $useremail = $q->param('email'); 

my $dbquery = "INSERT INTO contacts (id, lname, fname, phone, email) values
	('$userid', '$userfname', '$userlname', '$usernum', '$useremail')"; 
my $sth = $dbh->prepare($dbquery); 
$sth->execute; 

 print "Content-type: text/html\n\n";
 print "<html>\n<head>\n <title>Contact-Added</title>\n</head>\n<body>\n";
 print '<center><h2>All Contacts</h2></center>';
 print '<center><h3>Contact Added</h3></center>'; 
 print '<center><table border="1" width="800px">';
 #print header names
 print "<tr><th>ID</th><th>Name</th><th>Phone</th><th>Email</th></tr>"; 

my $sql = "select id, lname, fname, phone, email from contacts"; 
my $newsth = $dbh->prepare($sql);
$newsth->execute;

 while (my @row = $newsth->fetchrow_array) {
        print "<tr><td align='center'>$row[0]</td>
        <td align='center'>$row[2] $row[1]</td>
        <td align='center'>$row[3]</td>
        <td align='center'>$row[4]</td>
        </tr>\n";}
print "</table></center>\n";
print "<br><b1r><br><center><form><input type='button' value='Back' onclick='history.back()'></form></center>";
print "</body></html>\n";

 

