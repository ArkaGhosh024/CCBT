$(document).ready(function(){
	allEffects();
	$choice_text = $(".choice-text");
	$pre_text = $(".pre-text");
	$hidden_input = $("input[name=\"dialog\"]");
	$button_div = $(".button-div");
	$button_row = $(".button-row");
	
	$(document).on('click', '.choice-text', function (ev) {
	    ev.preventDefault();
		//console.log("reaching here");
		event.preventDefault();
		//appending option to conversation history
		//$conversation_history.append("<pre class=\"pull-left\" style=\"color:red\"><br>"+$(".bg-danger").text()+"<br></pre>");
		conversationHistoryRow("dialog", $(".bg-danger").text());
		//$conversation_history.append("<pre class=\"pull-right\" style=\"color:blue\"><br>"+$(this).text()+"<br></pre>");
		conversationHistoryRow("option", $(this).text());
		//$(".conversation-history-dialog").append("<p class=\"pull-left\" style=\"color:red\">"+$(".bg-danger").text()+"</p>");
		//$(".conversation-history-option").append("<p class=\"pull-right\" style=\"color:blue\">"+$(this).text()+"</p>");
		var $form = $("#conversation-form");
			option = parseInt($(this).attr('href'));
			dialog = $form.find("input[name=\"dialog\"]").val(),
			url = $form.attr("action"+"/");
			$.ajax({
				type: "POST",
				url: url,
				data: {
					//csrftoken: csrftoken, 
					option: option, 
					dialog: dialog
				},
				beforeSend: function(xhr){
					console.log("reaching here");
					xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
				},
				success:function(data){
					$to_be_updated = $(".to-be-updated");
					$to_be_updated.replaceWith("<div class=\"to-be-updated\">"+$(data).find(".to-be-updated").html()+"</div>");
					
					
					/*this little code should makes the dailog text fadeIn gradually and displays the user 
					options and avatar only after the entire text is displayed; but it is disabled because it was causing dialog to  
					be stored twice in history		
					*/
					allEffects();
					//setting focus on button once the history becomes long enough and the user has to scroll to get to the main dialog and option
					$('#user-avatar').focus();
					
				},
				
				error: function(xhr,errmsg,err){
					alert(xhr.status + ": " + xhr.responseText);
				}
		});
	});
});

var allEffects = function(){
	$dialog_text = $("#dialog-text");
	$user_avatar = $("#user-avatar");
	$choice_text = $(".choice-text");
	$choice_text.removeClass("hidden");
	$user_avatar.removeClass("hidden");
	$conversation_history = $(".conversation-history");
		/*
	$dialog_text.textillate({ 
		in: { 
			effect: 'fadeIn',
			delay: 5
		},
	});
	$dialog_text.on("end.tlt", function(){
		//I am having to use button class here but ideally I should be using $choice_text; this might lead to problems later on, keep a watch on it
		$choice_text.removeClass("hidden");
		$user_avatar.removeClass("hidden");
		$conversation_history = $(".conversation-history");
		//$conversation_history.append("<p>"+$dialog_text.text()+"</p>");
		//console.log($dialog_text.text());
	});*/
}

/*
see how to set images dynamically
*/
var conversationHistoryRow = function(type, text){
	if(type === "dialog"){
		//$conversation_history.append("<p class=\"pull-left\" style=\"color:red\"><br>"+text+"<br></p>");
		$conversation_history.append("<div class=\"row\">\
			<div class=\"col-lg-1 col-md-1 col-sm-2 col-xs-2\">\
				<img src=\"/static/conversationmanager/images/dummypatient_avatar/dummypatient_avatar.jpg\" style=\"width:50px;height:50px\" class=\"img-thumbnail img-responsive pull-left dummypatient-thumbnail-img\">\
			</div>\
			<div class=\"col-lg-10 col-md-10 col-sm-10 col-xs-10\">\
				<p class=\"pull-left bubble\" style=\"color:red\"><br>"+text+"<br></p>\
			</div>\
		</div>");
	}else if(type === "option"){
		$conversation_history.append("<div class=\"row\">\
			<div class=\"col-lg-11 col-md-11 col-sm-10 col-xs-10\">\
				<p class=\"pull-right bubble\" style=\"color:blue\"><br>"+text+"<br></p>\
			</div>\
			<div class=\"col-lg-1 col-md-1 col-sm-2 col-xs-2\">\
				<img src=\"/static/conversationmanager/images/therapist_avatar/therapist_avatar.png\" style=\"width:50px;height:50px\" class=\"img-thumbnail img-responsive pull-right\">\
			</div>\
		</div>");
	}
}

//src=\"images/dummypatient_avatar/dummypatient_avatar.jpg\"