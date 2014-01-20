//login for CoreGaming site
//Jesse Hoyt - jesselhoyt@gmail.com

//requires jQuery

$(document).ready(function(){

	$("#loginForm").submit(function(){

		//alert('Form Submitted') ;
		var username = $('#username').val() ;
		var password = $('#password').val() ;

		//alert('username: ' + username + ', password: ' + password) ;	

		if(username && password){ //check for values

			$.ajax({
				type: "GET",
				url: "login.cgi",
				dataType: "json",
				//send username and password as parameters to perl script
				data: "username=" + username + "&password=" + password,
				//script call Not successful
				error: function(XMLHttpRequest, textStatus, errorThrown){
					$('#loginResult').text("responseText: " + XMLHttpRequest.responseText 
            							+ ", textStatus: " + textStatus 
           							+ ", errorThrown: " + errorThrown);
          			$('#loginResult').addClass("error");				
				}, //error
				// script call successful
				//data contains JSON values returned by Perl script
				success: function(data){
					if (data.error) { // script returned error
            					$('#loginResult').text(data.error);
            					$('#loginResult').addClass("error");
          				} // if
         				else { // login was successful
            					//$('#loginForm').hide();
            					//$('#loginResult').text("Welcome " + data.username);
            					//$('#logout').show() ;
						//alert("sid: " + data.sid + ", loggedIn: " + data.loggedIn) ;
						//alert(location.href + "  " + location.pathname) ;
						location.href = location.href ;//refresh page to reveal changes
          				} //else
				}//success
			}) ;//ajax
		}//if
		else{
			$('#loginResult').text("enter username and password");
      			$('#loginResult').addClass("error");
    		} // else
    	$('#loginResult').fadeIn();
    	return false;
	}) ;

	$('#logout').click(function(){

		$.ajax({
			type: "GET",
			url: "logout.cgi",
			dataType: "json",
			error: function(XMLHttpRequest, textStatus, errorThrown){
					$('#loginResult').text("responseText: " + XMLHttpRequest.responseText 
            							+ ", textStatus: " + textStatus 
           							+ ", errorThrown: " + errorThrown);
          			$('#loginResult').addClass("error");
			},
			//data contains JSON values returned by perl script
			success: function(data){
				
				if (data.error){
					$('#loginResult').text(data.error);
            		$('#loginResult').addClass("error");
				}
				else{
					//$('#loginResult').text("") ;
					//$('#logout').hide() ;
					//$('#loginForm').show() ;
					//alert("sid: " + data.sid + ", loggedIn: " + data.loggedIn) ;
					location.href = location.href ;//refresh to reveal changes
				}

			}//success		
		}); //ajax
	}) ;

});

//checks if user is currently logged in
//returns JSON object with either true or false named field and a description string as value
//onTrue (function) : function to call if user logged in
//tArg (?) : argument to call onTrue with
//onFalse (function) : function to call if user is not logged in
//fArg (?) : argument to call onFalse with

function isLoggedIn(onTrue,tArg, onFalse, fArg){

	$.ajax({
		type: "GET",
		url: "isLoggedIn.cgi",
		dataType: "json",
		error: function(XMLHttpRequest, textStatus, errorThrown){
				$('#loginResult').text("responseText: " + XMLHttpRequest.responseText 
            						+ ", textStatus: " + textStatus 
           						+ ", errorThrown: " + errorThrown);
          		$('#loginResult').addClass("error");
		},
		//data contains JSON values returned by perl script
		//true or false named fields, with description string as value
		success: function(data){
			if(data.true){
				//alert(data.true) ;
				//alert(tArg) ;
				onTrue(tArg,data) ;
			}
			else{
				//alert(data.false) ;
				onFalse(fArg,data) ;
			}
		}//success
	});//ajax
} ;