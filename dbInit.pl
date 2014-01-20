#!/usr/bin/perl

use strict ;
use DBI ;

require "makeTable.pl" ;

my $dbh = DBI->connect(
"dbi:SQLite:dbname=database//CoreGaming.db",
"",
"",
{RaiseError => 1},
) or die $DBI::errstr;

$dbh->do("DROP TABLE IF EXISTS Games") ;
$dbh->do("CREATE TABLE Games(
	Title VARCHAR(255) NOT NULL,
	Console VARCHAR(255) NOT NULL,
	Price DECIMAL(6,2),
	NewOrUsed VARCHAR(255) NOT NULL,
	Quantity INT,
	Release TEXT,
	IconURL VARCHAR(255),
	Description VARCHAR(255),
	PRIMARY KEY (Title, Console, NewOrUsed)
)");
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', 'N64', 15.00, 'Used', 3, '1998-11-23',
 'Images\/The_Legend_of_Zelda_Ocarina_of_Time_box_art.png',
 'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff!')") ;
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', '3DS', 39.99, 'New', 10, '2011-06-19',
 'Images\/Legend-of-Zelda-Ocarina-of-Time-3D-Boxart.jpg',
 'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff! And now in 3D!')") ;
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', '3DS', 19.99, 'Used', 6, '2011-06-19',
 'Images\/Legend-of-Zelda-Ocarina-of-Time-3D-Boxart.jpg',
'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff! And now in 3D!')") ;

my $sth = $dbh->prepare("SELECT * FROM Games;");
$sth->execute() ;

print "Content-type:text/html\r\n\r\n";
print qq(
<!DOCTYPE html><html><head></head><body>);
 
=begin comment
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
=end comment
=cut

print makeTable($sth) ;
$sth->finish() ;
$dbh->disconnect() ;
print qq(
</body></html>);
1;