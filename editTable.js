//js file for editing CoreGaming table
//Jesse Hoyt - jesselhoyt@gmail.com

//requires Jquery
//requires Jquery ui(datepicker)

$(document).ready(function(){

	$('.edit').click(editClicked) ;
	

	$('#testLoggedIn').click(function(){

		isLoggedIn(function(){
			alert("Logged in") ;
		}, "",
		function(a,data){
			alert(a[0] + a[1] + a[2]) ;
			alert(data.false) ;
		}, ["Not", "Logged", "In"]) ;


	}) ;
}) ;

function editClicked(){

	
	isLoggedIn(function(e,data){
	
	if (cancelEdit()){ // don't continue if user chooses not to cancel ongoing edit
	var $editButtons = e.closest('div.editButtons') ;//find edit button's div
	e.remove() ;//remove edit button

	
	$editButtons.append($('<button class="save">Save</button><button class="cancel">X</button>'));//replace clicked edit button with cancel and save buttons
	$editButtons.children('.save').click(saveClicked) ;//add save and cancel buttons' click handlers
	$editButtons.children('.cancel').click(cancelClicked) ;

	//make fields editable
	var $game = $editButtons.siblings('.game') ;
	
	//save values in global variables to allow for reverting values
	var $title = $game.find('.title');
	title = $title.text() ;

	var $console = $game.find('.console') ;
	console = $console.text() ;

	var $description = $game.find('.description') ;
	description = $description.text() ;

	var $price = $game.find('.price') ;
	price = $price.text() ;

	var $newOrUsed = $game.find('.newOrUsed') ;
	newOrUsed = $newOrUsed.text() ;

	var $quantity = $game.find('.quantity') ;
	quantity = $quantity.text();

	var $release = $game.find('.release') ;
	release = $release.text() ;

	var $boxart = $game.find('.boxart') ;
	boxart = $boxart.text() ;

	var $priceInput = $('<input type="text" class="price" id="price" name="price"></input>') ;
	$priceInput.val(price) ;
	$price.replaceWith($priceInput) ;

	var $quantityInput = $('<input type="text" class="quantity" id="quantity" name="quantity"></input>');
	$quantityInput.val(quantity) ;
	$quantity.replaceWith($quantityInput) ;

	var $releaseInput = $('<input type="text" class="release" id="realease" name="release"></input>') ;
	$releaseInput.val(release) ;
	$releaseInput.datepicker({dateFormat: "M dd, yy"} ) ;
	$release.replaceWith($releaseInput) ;
	
	
	var $descriptionInput = $('<textarea class="description" id="description" name="description"></textarea>') ;
	$descriptionInput.val(description) ;
	$description.replaceWith($descriptionInput) ;
	}	

	},$(this), function(f,data){
		alert(data.false);
		//show login form again so user can log in
		$('#loginForm').show() ;
		$('#loginResult').text(" ") ;
		$('#logout').hide() ;
		
	},"") ;	

}

//cancels ongoing edits if they exist and user chooses to
//force (boolean) : if true doesn't ask user, just cancels edits
//returns true if edit was cancelled or no edit ongoing, false if edit was not cancelled
function cancelEdit(force){

	var $priceInput = $('input.price') ;
	
	if($priceInput.length === 0){
		return true ;//no edits to cancel
	}else if(force || confirm("Are you sure you want to cancel changes?")){//check if user wants to cancel current edit

		//replace inputs with previous elements
		var $price = $('<h4 class="price"></h4>') ;
		$price.text(price) ;
		$priceInput.replaceWith($price) ;

		var $quantityInput = $('input.quantity') ;
		var $quantity = $('<h4 class="quantity"></h4>') ;
		$quantity.text(quantity) ;
		$quantityInput.replaceWith($quantity) ;

		var $releaseInput = $('input.release') ;
		var $release = $('<h4 class="release"></h4>') ;
		$release.text(release) ;
		$releaseInput.replaceWith($release) ;

		var $descriptionInput = $('textarea.description') ;
		var $description = $('<p class="description"></p>') ;
		$description.text(description) ;
		$descriptionInput.replaceWith($description) ;

		//remove save, cancel buttons, replace with edit button
		var $saveCancel = $(".save").parent() ;//find parent of any active save, cancel buttons to remove them
		$saveCancel.find(".save").remove() ;
		$saveCancel.find(".cancel").remove() ;
		$saveCancel.append($('<button class="edit">Edit</button>')) ;//append edit button where old save, cancel buttons were
		$saveCancel.children('.edit').click(editClicked);//attach edit button's click handler

		return true ;//edit was cancelled
	}else{
		return false ;//edit was not cancelled
	}
}

//save current edits
//e (event) : button pressed to save edit, used to find input fields
function saveEdit(e){
	
	
	$(".error").remove() ;//clear any errors
	
	var $editButtons = e.closest('div.editButtons') ;//find edit button's div
	var $game = $editButtons.siblings('.game') ;//find game being edited
	
	//NEED TO:
	//VALIDATE input
	//ADD ability to Update Boxart
	
	//alert($game.find('.description').val()) ;
	
	//Validate input
	var valid = true ;
	
	//Price validation
	var priceRegex = new RegExp(/^\d*(\.\d{2})?$/) ;
	var price = $game.find('.price').val() ;
	var price_float = parseFloat(price) ;
	//alert(priceRegex.test(price)) ;
	if(isNaN(price_float) || !priceRegex.test(price)){//check that price represents a float, if not...
		valid = false ;
		$game.find('.priceWrapper').append($('<div class="error">Price must be a number.</div>'));
		//alert("price must be a number") ;
		}
		
	//Date validation
	
	var dateRegex = new RegExp(/^[a-zA-Z]{3} \d{2}, \d{4}$/) ;
	var releaseDate = $game.find('.release').val() ;
	if(!dateRegex.test(releaseDate)){
		valid = false ;
		$game.find('.releaseWrapper').append($('<div class="error">Invalid Date. Expected Format: Mon dd, yyyy</div>'));
		//alert("Invalid Date") ;
	}
	
	//format date for database
	var $formatedDate = $.datepicker.formatDate("mm:dd:yy",new Date(releaseDate)) ;
	
	//Quantity validation
	
	var quantityRegex = new RegExp(/^\d*$/) ;
	var quantity = $game.find('.quantity').val() ;
	var quantity_int = parseInt(quantity) ;
	
	if(isNaN(quantity_int) || !quantityRegex.test(quantity)){
		valid = false ;
		$game.find('.quantityWrapper').append($('<div class="error">Quantity must be a number.</div>'));
	
	}
	
	if(valid){
		$.ajax({
			type: "GET",
			url: "saveEdit.cgi",
			dataType: "json",
			data: "title=" + $game.find('.title').text() + "&console=" + $game.find('.console').text() + "&boxart=" + $game.find('.boxart').attr('src') +
			"&price=" + parseFloat($game.find('.price').val()) + "&newOrUsed=" + $game.find('.newOrUsed').text() +
			"&quantity=" + $game.find('.quantity').val() + "&release=" + $formatedDate + "&description=" + $game.find('.description').val(),
			error: function(XMLHttpRequest, textStatus, errorThrown){
						$('#loginResult').text("responseText: " + XMLHttpRequest.responseText 
											+ ", textStatus: " + textStatus 
										+ ", errorThrown: " + errorThrown);
						$('#loginResult').addClass("error");				
					},
			success: function(data){
						if (data.error) { // script returned error
									$('#loginResult').text("data.error: " + data.error);
									$('#loginResult').addClass("error");
							}
						else {
							alert("Changes saved to database") ;
							location.href = location.href ;//refresh to show changes
						}}
		});//ajax
	}//if
		
}

function saveClicked(){
alert("saving");

isLoggedIn(saveEdit, $(this), function(f, data){
		alert(data.false);
		//show login form again so user can log in
		$('#loginForm').show() ;
		$('#loginResult').text(" ") ;
		$('#logout').hide() ;
		}, "") ;
}

function cancelClicked(){
	cancelEdit()
}