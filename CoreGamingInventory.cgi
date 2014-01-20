#!/usr/bin/perl

use DBI ;

require "CoreGamingHeader.pl" ;
require "makeTable.pl" ;

print "Content-type:text/html\r\n\r\n";
print qq(
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Core Gaming Inventory</title>
<link rel="stylesheet" href="CoreGaming.css"/>
<link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/redmond/jquery-ui.min.css" rel="stylesheet" type="text/css" />
<script src="/resources/jquery-1.9.1.min.js"></script>
<script src="/resources/jquery-ui-1.10.3.custom.min.js"></script>
<script src="login.js"></script>
<script src="editTable.js"></script>
</head>
<body>
);
print coreGamingHeader() ;

#connect to inventory database
my $dbh = DBI->connect(
"dbi:SQLite:dbname=database//CoreGaming.db",
"",
"",
{RaiseError => 1},
) or die $DBI::errstr;

#query database for all games
my $sth = $dbh->prepare("SELECT * FROM Games;") ;
$sth->execute ;

#print makeTable($sth) ;
print '<h3>Site is a work in progress. Inventory in no way reflects actual pricing or availablility of games</h3>' ;
print '<button name="testLoggedIn" id="testLoggedIn">Test isLoggedIn</button>' ;
print makePrettyTable($sth) ;
print qq(

</body>
</html>
);
1;
