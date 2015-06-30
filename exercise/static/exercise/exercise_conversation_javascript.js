$(document).ready(function(){
	//confirm("reaching here");
	var moduleId = $("input[name=\"module-specific-message\"]").val();
	$module_specific_message = $(".module-specific-message");
	//console.log($module_specific_message.text());
	setMessage(moduleId);
});

var setMessage = function(moduleId){
	var message;
	switch(moduleId){
		case '1':
		message = "Psychoeducation";
		break;
		case '2':
		message = "Behavioral Activation";
		break;
		case '3':
		message = "Identifying NATs";
		break;
		case '4':
		message = "Challenging NATs";
		break;
		case '5':
		message = "Modifying Intermediate and Core Beliefs";
		break;
		case '6':
		message = "Relapse Prevention";
		break;
	}
	$module_specific_message.text(message);
}