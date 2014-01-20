#!/usr/bin/perl
#login for Core Gaming
#Jesse Hoyt - jesselhoyt@gmail.com

use CGI ;
use DBI ;
use warnings ;

#read CGI params
my $cgi = CGI->new ;
my $username = $cgi->param("username") ;
my $password = $cgi->param("password") ;

#connect to database

my $dbh = DBI->connect("dbi:SQLite:dbname=database//CoreGaming.db","","", {RaiseError => 1},)
 or die $DBI::errstr ;

#query db for username and password

my $sth = $dbh->prepare("SELECT username FROM Users WHERE username = ? AND password = ?");
 
$sth->execute($username, $password); 
 

my ($returnedUsername) = $sth->fetchrow_array ;

#create JSON string for database result

my $json = ($returnedUsername) ?
	qq{{"success" : "login is successfull", "username" : "$returnedUsername"}} :
	qq{{"error" : "username or password is wrong"}};

#return JSON string
print $cgi->header(-type => "application/json", -charset => "utf-8") ;
print $json ;
