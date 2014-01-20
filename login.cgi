#!/usr/bin/perl
#login for Core Gaming
#Jesse Hoyt - jesselhoyt@gmail.com

use CGI ;
use CGI::Session ;
use DBI ;
use strict ;
use warnings ;

#read CGI params
my $cgi = CGI->new ;
my $username = $cgi->param("username") ;
my $password = $cgi->param("password") ;

#retrieve/create session
my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) || die CGI::Session->errstr() ;
my $sid = $session->id() ;

#store userName in session
$session->param("userName", $username) ;

#connect to database

my $dbh = DBI->connect("dbi:SQLite:dbname=database//CoreGaming.db","","", {RaiseError => 1},)
 or die $DBI::errstr ;

#query db for username and password

my $sth = $dbh->prepare("SELECT username FROM Users WHERE username = ? AND password = ?")
 or die $DBI::errstr ;
$sth->execute($username, $password) 
 or die $DBI::errstr ;

my ($returnedUsername) = $sth->fetchrow_array ;

#set loggedIn field of session
my $loggedIn = ($returnedUsername)?1:0 ;
$session->param("loggedIn", $loggedIn) ;

#set loggedIn to expire after 10 minutes of inaction
$session->expire("loggedIn", "+10m") ;


#create JSON string for database result

my $json = ($returnedUsername) ?
	qq{{"success" : "login is successful", "username" : "$returnedUsername", "sid" : "$sid", "loggedIn" : "$loggedIn"}} :
	qq{{"error" : "username or password is wrong"}};

#return JSON string

print $session->header(-type => "application/json", -charset => "utf-8") ;
print $json ;
$session->flush() ;