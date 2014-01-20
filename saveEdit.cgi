#!/usr/bin/perl
#save edits to database for Core Gaming
#Jesse Hoyt - jesselhoyt@gmail.com
#11/09/2013

use CGI ;
use CGI::Session ;
use DBI ;
use strict ;
use warnings ;

my $json = "" ;#json string to return

#read CGI params
my $cgi = CGI->new ;
my @names = $cgi->param ;

#retrieve/create session
my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) || die CGI::Session->errstr();

if($session->param("loggedIn")){

	#connect to database
	my $dbh = DBI->connect("dbi:SQLite:dbname=database//CoreGaming.db", "", "", {RaiseError => 1},)
	or die $DBI::errstr ;
	
	my $title = $cgi->param("title") ;
	my $console = $cgi->param("console") ;
	my $newOrUsed = $cgi->param("newOrUsed") ;
	my $price = $cgi->param("price") ;
	$price = $price + 0.0 ;
	my $quantity = $cgi->param("quantity") ;
	$quantity = int($quantity) ;
	my $release = $cgi->param("release") ;
	my $description = $cgi->param("description") ;
	
	
	#update entry
	my $sth = $dbh->prepare("UPDATE Games SET Price = ?, Quantity = ?, Release = ?, Description = ?
		WHERE Title = ? AND Console = ? AND NewOrUSed = ?")
		or die $DBI::errstr ;
	$sth->execute($price, $quantity, $release, $description, $title , $console, $newOrUsed)
		or die $DBI::errstr ;
		
	$json = qq{{"success" : "Database updated."}} ;

}
else{

	$json = qq{{"error" : "Log in to be able to save changes."}};

}
print $session->header(-type => "application/json", -charset => "utf-8") ; 
print $json ;
