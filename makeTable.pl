#!/usr/bin/perl

use DBI ;
use CGI ;
use CGI::Session ;

#use feature "switch" ;
#use enum qw(Jan=01 Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec) ;

#makeTable(statement handler)
#returns a string for a html table of the results of a SQL query

sub makeTable {

	my $sth = shift ;

	my @labels = @{$sth->{NAME}} ;

	my $str = '<table border="1"><tr>';
	for my $label (@labels){
		$str.= '<th>'.$label.'</th>';
	}
	$str.= '</tr>';

	my $res = $sth->fetchall_arrayref() ;
	my $numColumns = @{$$res[0]} ;

	for my $row (@$res){
		
		$str.= '<tr>' ;
		for (my $i = 0 ; $i < $numColumns ; $i++){
			$str.='<td>' ;
			if($labels[$i] eq 'Price'){
				$str.= sprintf ("\$%.2f\</td\>", $$row[$i]) ;
			}
			
			else{
				$str.= $$row[$i].'</td>' ;
			}
		}
		$str.='</tr>' ;
	}
	$str.='</table>' ;

	return $str ;

	
}

#formatDate(date)
#formats date for printing as Mon dd, yyyy
#date : date string in the format mm:dd:yyyy
sub formatDate{

	my $date = shift ;

	my $ret = "" ;
	$month = substr $date, 0, 2 ;
		
		if ($month eq "01"){$ret.="Jan";}
		elsif ($month eq "02"){$ret.="Feb";}
		elsif ($month eq "03"){$ret.="Mar";}
		elsif ($month eq "04"){$ret.="Apr";}
		elsif ($month eq "05"){$ret.="May";}
		elsif ($month eq "06"){$ret.="Jun";}
		elsif ($month eq "07"){$ret.="Jul";}
		elsif ($month eq "08"){$ret.="Aug";}
		elsif ($month eq "09"){$ret.="Sep";}
		elsif ($month eq "10"){$ret.="Oct";}
		elsif ($month eq "11"){$ret.="Nov";}
		elsif ($month eq "12"){$ret.="Dec";}
	

	$ret.= " ".(substr $date, 3, 2).", ".(substr $date, 6, 4) ;
	return $ret ;

}

#makePrettyTable(statement handler)
#returns a string for a html table of the results of a SQL query
#formatted especially for displaying games

sub makePrettyTable {

	my $cgi = CGI->new ;
	my $session = new CGI::Session("driver:File", $cgi, {Directory=>'/tmp'}) ;
	if(! defined $session){

		die CGI::Session->errstr() ;

	}
	my $username = $session->param("userName") ;
	my $loggedIn = $session->param("loggedIn") ;
	if (! defined $loggedIn){#loggedIn param undefined, meaning new session
		$loggedIn = 0 ;
		$session->param("loggedIn", $loggedIn) ;
	}


	my $sth = shift ;

	my @labels = @{$sth->{NAME}} ;

	my $str = '<table border="1" class="gameTable">' ;

	my $res = $sth->fetchall_arrayref() ;
	my $numColumns = @{$$res[0]} ;
	my $numItems = @$res ;

	for(my $i = 0 ; $i < $numItems ; $i++){
		
		#keep rows 5 across
		if(($i == 0) || (($i % 5) == 0)){
			$str.= '<tr>' ;
		}
		$str.='<td>' ;
		if($loggedIn){#only show edit buttons if user logged in
			$str.='<div class="editButtons"><button class="edit">Edit</button></div>' ;
		}

		my $item = $$res[$i] ;

		$str.='<div class="game">' ;
		my $title = $$item[0] ;
		my $console = $$item[1] ;
		my $price = $$item[2] ;
		my $newOrUsed = $$item[3] ;
		my $quantity = $$item[4] ;
		my $release = $$item[5] ;
		my $img = $$item[6] ;
		my $description = $$item[7] ;
	
		$str.='<img src="' . $img.'" class="boxart"><div class="titleConsole"><h3 class="title">'.$title.'</h3><h4 class="console">'.$console.'</h4></div>
		<div class="details"><div class="priceWrapper"><label>$</label><h4 class="price">'. sprintf ("%.2f", $price).'</h4></div><h4 class="newOrUsed">'.
		$newOrUsed.'</h4><div class="quantityWrapper"><label>Quantity:</label><h4 class="quantity">'.$quantity.'</h4></div></br>
		<div class="releaseWrapper"><label>Released:</label><h4 class="release">'.
		formatDate($release).'</h4></div></div><div class="descriptionWrapper"><p class="description">'.$description.'</p></div>';

		$str.='</div></td>' ;

		#end row after 5th item or last item
		if(($i != 0) &&(($i % 6) == 0) || $i == ($numItems - 1)){
			$str.= '</tr>' ;
		}

	}
	$str.= '</table>' ;
	return $str ;
}

1;