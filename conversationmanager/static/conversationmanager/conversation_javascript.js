$(document).ready(function(){
	allEffects();
	$choice_text = $(".choice-text");
	$pre_text = $(".pre-text");
	$hidden_input = $("input[name=\"dialog\"]");
	$button_div = $(".button-div");
	$button_row = $(".button-row");
	var backgroundColor = "white";
	var saveConversationHistory = "";
	var currentDialogId=0;
	var dummyPatientDialogArray = [];
	dummyPatientDialogArray[currentDialogId++] = $("#dialog-text").text();
	console.log(dummyPatientDialogArray);
	var wrongConversationStartId = 0;
	
	$(document).on('click', '.choice-text', function (ev) {
	    ev.preventDefault();
		//console.log("reaching here");
		//event.preventDefault();
		//appending option to conversation history

		var dialogHistoryText = $(".currentdialog").text();
		saveConversationHistory+=">DP:"+dialogHistoryText+";\n";
		var optionHistoryText =  $(this).text();
		saveConversationHistory+=">U:"+optionHistoryText+";\n";

		conversationHistoryRow("dialog", dialogHistoryText, backgroundColor, currentDialogId);
		conversationHistoryRow("option", optionHistoryText, backgroundColor, currentDialogId);
		
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
					dummyPatientDialogArray[currentDialogId++] = $("#dialog-text").text();
					console.log(dummyPatientDialogArray);
					repeatedDialog(dummyPatientDialogArray);
					/*this little code should makes the dailog text fadeIn gradually and displays the user 
					options and avatar only after the entire text is displayed; but it is disabled because it was causing dialog to  
					be stored twice in history		
					*/
					allEffects();
					//setting focus on button once the history becomes long enough and the user has to scroll to get to the main dialog and option
					//$('.choice-text').focus();
					//$("html, body").animate({ scrollTop: $("#user-avatar").scrollTop() }, 1000);
					//the following line makes the page scroll down to the bottom of the page
					$("html, body").animate({ scrollTop: $(document).height() }, 500);
					
					if(parseInt($("a[name=\"option\"]").attr('href'))){
						console.log(parseInt($("a[name=\"option\"]").attr('href')));
					}else{
						console.log("conversation ended");
						$(".button-row").replaceWith("<button class=\"btn btn-success pull-right\" id=\"finish-btn\">Finish!</button>");
					}
					
				},
				
				error: function(xhr,errmsg,err){
					alert(xhr.status + ": " + xhr.responseText);
				}
			});
	});
	
	$(document).on('click', '#finish-btn', function (ev) {
		ev.preventDefault();
		
		confirm("show next conversation");
		var dialogHistoryText = $(".bg-danger").text();
		saveConversationHistory+=">DP:"+dialogHistoryText+";\n";
		console.log(saveConversationHistory);
		var url = "/history/"
		var conversationID = $("input[name=\"conversationID\"]").val();
		$.ajax({
				type: "POST",
				url: url, //get the url here
				data: {
					//csrftoken: csrftoken, 
					history: saveConversationHistory, 
					conversationID: conversationID,
				},
				beforeSend: function(xhr){
					console.log("reaching here");
					xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
				},
				success:function(data){
					console.log("conversation history sent to backend");
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

var conversationHistoryRow = function(type, text, backgroundColor, currentDialogId){
	if(type === "dialog"){
		//console.log(dummyPatientDialogArray);
		//$conversation_history.append("<p class=\"pull-left\" style=\"color:red\"><br>"+text+"<br></p>");
		$conversation_history.append("<div class=\"row\">\
			<div class=\"col-lg-1 col-md-1 col-sm-2 col-xs-2\">\
				<img src=\"/static/conversationmanager/images/dummypatient_avatar/dummypatient_avatar.jpg\" style=\"width:50px;height:50px\" class=\"img-thumbnail img-responsive pull-left dummypatient-thumbnail-img\">\
			</div>\
			<div class=\"col-lg-10 col-md-10 col-sm-10 col-xs-10\">\
				<p class=\"pull-left bubbledummypatient\" id=\"dialog"+(currentDialogId-1)+"\"><br>"+text+"<br></p>\
			</div>\
		</div>");
	}else if(type === "option"){
		$conversation_history.append("<div class=\"row\">\
			<div class=\"col-lg-11 col-md-11 col-sm-10 col-xs-10\">\
				<p class=\"pull-right bubbleuser\" id=\"choice"+(currentDialogId-1)+"\"><br>"+text+"<br></p>\
			</div>\
			<div class=\"col-lg-1 col-md-1 col-sm-2 col-xs-2\">\
				<img src=\"/static/conversationmanager/images/therapist_avatar/therapist_avatar.png\" style=\"width:50px;height:50px\" class=\"img-thumbnail img-responsive pull-right\">\
			</div>\
		</div>");
	}
}

//the following method checks for repeated 
var latestWrongConversationId = 0;
var repeatedDialog = function(dialogArray){
	var currentDialogString = dialogArray[dialogArray.length-1];
	console.log(currentDialogString);
	for(var i=dialogArray.length-2; i>=latestWrongConversationId; i--){
		if(dialogArray[i] === currentDialogString){
			//alert("reaching here");
			wrongConversationStartId = i;
			latestWrongConversationId = (dialogArray.length-1);
			console.log(wrongConversationStartId+";"+(dialogArray.length-1));
			redMarkWrongConversation((wrongConversationStartId+1), dialogArray.length-1);
			break;
		}
	}
}

var redMarkWrongConversation = function(i, j){
	for(var k=i; k<=j; k++){
		$("#dialog"+k).addClass("wrongConversation");
		$("#choice"+k).addClass("wrongConversation");
	}
}