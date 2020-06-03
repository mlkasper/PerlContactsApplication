#!/usr/bin/perl -w

use strict; 
use warnings; 
use DBI; 
use CGI qw(:standard); 

my $dsn = "DBI:mysql:USERNAME"; 
my $username = "root"; 
my $password = "PASSWORD"; 

my %attr = (PrintError =>0, RaiseError=>1); 
my $dbh = DBI->connect($dsn, $username, $password, \%attr);

my $option = param('options'); 


#check that the user selected "Show All Contacts"
if($option eq "print") {

 print "Content-type: text/html\n\n";
 print "<html>\n<head>\n <title>View All Entries</title>\n</head>\n<body>\n";
 my $sql = q/select id, lname, fname, phone, email from contacts/;
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
}

if($option eq "search") {

  print "Content-type: text/html\n\n";
  print "<html>\n<head>\n <title>Search for Contact</title>\n</head>\n<body>\n";

  print "<center><h1>Search</h1>
	<h3 style='strong'>Search by last name:</h3>
	<form METHOD=POST ACTION='../cgi-bin/search.cgi'>
	<input TYPE=TEXT NAME=lname SIZE=40 maxlength=40>
	<BR><BR>
	<input TYPE=submit name=submit value='Submit'>
	<input TYPE=button value='Back' onclick='history.back()'>
	</form></center>"; 	

  print"</body></html>\n";
}
if($option eq "add") {
  print "Content-type: text/html\n\n";
  print "<html>\n<head>\n <title>Add Contacts</title>\n</head>\n<body>\n";
  print "<center><h1>Add a Contact</center>
        <form METHOD=POST ACTION='../cgi-bin/add.cgi'>
	<center>ID: <input TYPE=number name=id>
	First Name: <input TYPE=TEXT name=lname>
	Last Name: <input TYPE=TEXT name=fname>
	Phone Number: <input TYPE=number name=number>
	Email: <input TYPE=TEXT name=email><br><br>
	<input TYPE=submit name=submit value='Submit'>
	<input TYPE=button value='Back' onclick='history.back()'>
</center>"; 
}
if($option eq "delete") {

  print "Content-type: text/html\n\n";
  print "<html>\n<head>\n <title>View All Entries</title>\n</head>\n<body>\n"    ;
  my $sql = q/select id, lname, fname, phone, email from contacts/;
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
print "<br><br><center><form method=POST action=../cgi-bin/delete.cgi'>
<br><br><input type='text' name='uid'><input type=submit value='Submit'>

<input type='button' value='Back' onclick='history.back()'></form></center>
"; 
print "</body></html>\n";
}
if($option eq 'update'){
 print "Content-type: text/html\n\n";
 print "<html>\n<head>\n <title>Edit Contact</title>\n</head>\n<body>\n";
 my $sql = q/select id, lname, fname, phone, email from contacts/;
my $sth = $dbh->prepare($sql);
$sth->execute;
print '<center><h2>Edit Contact</h2></center>';
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
print "<br><br><center>
<form METHOD=POST ACTION='../cgi-bin/edit.cgi'>
<br>Enter an ID to edit that Contact: <input type=number name='idin'>
<br><br><input type='submit' name=submit value='Submit'>
<input type='button' value='Back' onclick='history.back()'>
</form></center>";
print "</body></html>\n";
}
$dbh->disconnect(); 
