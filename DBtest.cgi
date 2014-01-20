#!/usr/bin/perl

use strict ;
use DBI ;

my @ary = DBI->available_drivers() ;
print "Content-type:text/html\r\n\r\n";
print qq(
<!DOCTYPE html><html><head></head><body>);
print '<p>'.join('<br/>', @ary) . '</p>';
my $dbh = DBI->connect(
"dbi:SQLite:dbname=database//test.db",
 "",
 "",
 {RaiseError => 1},
) or die $DBI::errstr;

if($dbh){
	print '<p>connected</p>' ;
}
else{
	print '<p>not connected</p>' ;
}
 

my $sth = $dbh->prepare("SELECT SQLITE_VERSION();");
$sth->execute() ;

my $ver = $sth->fetch() ;

print '<p>'.$$ver[0].'</p>' ;
$sth->finish() ;

$dbh->do("DROP TABLE IF EXISTS Cars");
$dbh->do("CREATE TABLE Cars(Id INT PRIMARY KEY, Name TEXT, Price INT)");
$dbh->do("INSERT INTO Cars VALUES(1,'Audi',52642)");
$dbh->do("INSERT INTO Cars VALUES(2,'Mercedes',57127)");
$dbh->do("INSERT INTO Cars VALUES(3,'Skoda',9000)");
$dbh->do("INSERT INTO Cars VALUES(4,'Volvo',29000)");
$dbh->do("INSERT INTO Cars VALUES(5,'Bentley',350000)");
$dbh->do("INSERT INTO Cars VALUES(6,'Citroen',21000)");
$dbh->do("INSERT INTO Cars VALUES(7,'Hummer',41400)");
$dbh->do("INSERT INTO Cars VALUES(8,'Volkswagen',21600)");

$sth = $dbh->prepare("SELECT * FROM Cars;");
$sth->execute() ;
 
print '<table><tr>';
for my $fields (@{ $sth->{NAME}}){
	print '<td>'.$fields.'</td>';
}
print '</tr>';
my $res = $sth->fetchall_arrayref() ;
for my $rowref (@$res){
	print '<tr>' ;
	for my $val (@$rowref){
		print '<td>'.$val.'</td>';
	}
print '</tr>';
}
print '</table>';

$sth->finish() ;
$dbh->disconnect() ;
print qq(
</body></html>);
1;