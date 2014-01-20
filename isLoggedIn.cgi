#!/usr/bin/perl

use DBI ;
use CGI ;
use CGI::Session ;

my $json = "" ;
my $cgi = CGI->new ;
my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) ||	die CGI::Session->errstr() + "!!!!!!!!!!!!!!!!!!!" ;


if($session->is_expired){
	$json = qq{{"false" : "Session expired! Please refresh page and log back in."}} ;
}
elsif(($session->param("loggedIn")) == 1){
	$json = qq{{"true" : "Logged in."}} ;
}
else
{
	$json = qq{{"false" : "Please Login."}} ;
}

print $session->header(-type => "application/json", -charset => "utf-8") ;
print $json ;