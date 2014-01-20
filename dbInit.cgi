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
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', 'N64', 15.00, 'Used', 3, '11:23:1998',
 'Images\/The_Legend_of_Zelda_Ocarina_of_Time_box_art.png',
 'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff!')") ;
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', '3DS', 39.99, 'New', 10, '06:19:2011',
 'Images\/Legend-of-Zelda-Ocarina-of-Time-3D-Boxart.jpg',
 'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff! And now in 3D!')") ;
$dbh->do("INSERT INTO Games VALUES('Legend of Zelda:Ocarina of Time', '3DS', 19.99, 'Used', 6, '06:19:2011',
 'Images\/Legend-of-Zelda-Ocarina-of-Time-3D-Boxart.jpg',
'Ocarina of Time is only like the greatest game ever! It&apos;s super awesome and stuff! And now in 3D!')") ;
$dbh->do("INSERT INTO Games VALUES('Metal Gear Solid 2', 'PS2', 14.99, 'Used', 3, '11:12:2001',
 'Images\/Metalgear2boxart.jpg',
'The Stealth-tastic game from Hideo Kojima. Snaaaaake!')") ;
$dbh->do("INSERT INTO Games VALUES('Metal Gear Solid 3:Snake Eater', 'PS2', 19.99, 'Used', 5, '11:17:2004',
 'Images\/Mgs3box.jpg',
'The Stealth-tastic game from Hideo Kojima.And now with snake eating action! Snaaaaake!')") ;
$dbh->do("INSERT INTO Games VALUES('Metal Gear Solid 4:Guns of the Patriots', 'PS3', 39.99, 'Used', 4, '06:12:2008',
 'Images\/Mgs4_cover.jpg',
'The Stealth-tastic game from Hideo Kojima. Snaaaaake!')") ;
$dbh->do("INSERT INTO Games VALUES('Metal Gear Solid 4:Guns of the Patriots', 'PS3', 49.99, 'New', 1, '06:12:2008',
 'Images\/Mgs4_cover.jpg',
'The Stealth-tastic game from Hideo Kojima. Snaaaaake!')") ;


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