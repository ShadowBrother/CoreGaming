#!usr/bin/perl

use CGI ;
use CGI::Session ;
use strict ;
use warnings ;



sub coreGamingHeader {

my $cgi = CGI->new ;
my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) || die CGI::Session->errstr() ;

my $username = $session->param("userName") ;
my $loggedIn = $session->param("loggedIn") ;
if (! defined $loggedIn){#loggedIn param undefined, meaning new session
	$loggedIn = 0 ;
	$session->param("loggedIn", $loggedIn) ;
	$session->expire("+1w") ;#session expires after 1 week
	#set loggedIn to expire after 10 minutes of inaction
	$session->expire("loggedIn", "+10m") ;
}

my $ret = qq {
<header>
<a href="index.cgi"><img id="logo" src="CoreGamingLogoEnhanced.gif"></a>
<div id="details">
<p>5 North Broadway Salem, New Hampshire</p>
<dl>
<dt>Phone</dt>
<dd>(603) 458-5791</dd>
<dt>Email</dt>
<dd><a href="mailto:matt.coregaming&#64;yahoo.com">matt.coregaming&#64;yahoo.com</a></dd>
</dl>
</div>
<div id="login">
<form id="loginForm" name="loginForm" method="post" action="" } ;

#if user logged in, hide login form
if ($loggedIn){
	$ret .= "hidden" ;
	

}

$ret .= qq {>
<label for="username">UserName</label>
<input type="text" id="username" name="username" required="required" placeholder="Username">
<br/>
<label for="password">Password</label>
<input type="password" id="password" name="password" required="required" placeholder="Password">
<br />
<button type="submit">Login</button>
</form>
<div id="loginResult">} ;
#if user logged in, show welcome
if($loggedIn){
	$ret .= "Welcome $username" ;
}
$ret.= qq{</div>
<div id="logout" } ;
#if user not logged in, hide logout link
if (! $loggedIn){
	$ret .= "hidden" ;
}

$ret .= qq{>Logout</div>
</div>
</header>
<ul id="tabs">
<li><a href="index.cgi">Home</a></li>
<li><a href="CoreGamingInventory.cgi">Inventory</a></li>
</ul>
} ;
$session->flush() ;
return $ret ;
}
1;