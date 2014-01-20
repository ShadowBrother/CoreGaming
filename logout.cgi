#!/usr/bin/perl
#logout Core Gaming
#Jesse Hoyt - jesselhoyt@gmail.com

use CGI ;
use CGI::Session ;
use strict ;
use warnings ;


my $cgi = CGI->new ;
#retrieve session
my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) ;
my $sid = $session->id() ;

$session->param("loggedIn", 0) ;
my $loggedIn = $session->param("loggedIn") ;
print $session->header(-type => "application/json", -charset => "utf-8") ;
print qq({"success" : "user logged out", "sid" : "$sid", "loggedIn" : "$loggedIn"}) ;