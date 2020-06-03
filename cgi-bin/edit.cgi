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

my $input = param('idin');

print "Content-type: text/html\n\n";
print "<html>\n<head>\n <title>Search Results</title>\n</head>\n<body>\n";

my $sql = "select id, lname, fname, phone, email from contacts where id='$input'";
my $sth = $dbh->prepare($sql);
$sth->execute;

print "<center><form METHOD=POST ACTION='../cgi-bin/add2.cgi'>";
print "<h1>Edit Contact</h1><hr><br>";
my @row = $sth->fetchrow_array;
print "
	ID: <input type=number name='num' value='$row[0]'>
	   First Name: <input type=TEXT name=fname value='$row[2]'>
	   Last Name: <input type=TEXT name=lname value='$row[1]'>
	   Phone: <input type=number name=phone value='$row[3]'>
	   Email: <input type=TEXT name=email value='$row[4]'>"; 

print "<br><br><input type=submit value='Submit Changes'>
       <input type=button value='Back' onclick='history.back()'>";
print "</center></body></html>";

 
