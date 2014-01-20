#!/usr/bin/perl

require "CoreGamingHeader.pl" ;

print "Content-type:text/html\r\n\r\n";
print qq(
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Core Gaming</title>
<link rel="stylesheet" href="CoreGaming.css"/>
<script src="/resources/jquery-1.9.1.min.js"></script>
<script src="login.js"></script>
</head>
<body>
);
print coreGamingHeader() ;
print qq(
<div id="body">
<h2>Come on down for all your used game needs!</h2>
) ;
print qq(
</div>
<!--google map --!>
<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=5+North+Broadway+Salem,+New+Hampshire&amp;aq=&amp;sll=42.512602,-70.114746&amp;sspn=6.235225,16.907959&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=5+N+Broadway,+Salem,+New+Hampshire+03079&amp;ll=42.791244,-71.226854&amp;spn=0.022045,0.036478&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe><br /><small><a href="https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=5+North+Broadway+Salem,+New+Hampshire&amp;aq=&amp;sll=42.512602,-70.114746&amp;sspn=6.235225,16.907959&amp;t=h&amp;ie=UTF8&amp;hq=&amp;hnear=5+N+Broadway,+Salem,+New+Hampshire+03079&amp;ll=42.791244,-71.226854&amp;spn=0.022045,0.036478&amp;z=14&amp;iwloc=A" style="color:#0000FF;text-align:left">View Larger Map</a></small>
</body>
</html>
);
1;
