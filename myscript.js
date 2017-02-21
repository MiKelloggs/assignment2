var sendDataToServer = function(){
	var request = new XMLHttpRequest();
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log("hey, something worked");
			} else {
				console.error("that didnt work...");
			}
		}
	};
	
	var userInput = document.getElementById("textinput");
	var inputValue = userInput.value;
	var data = "message=" + encodeURIComponent(inputValue);
	
	request.open("POST", "http://localhost:8080/plants");
	request.send(data);
};

var myButton = document.getElementById("myButton");
	myButton.onclick = function () {
	console.log("the button was clicked!");
	sendDataToServer();
	getDataFromServer();
};




var getDataFromServer = function(){
	  var request = new XMLHttpRequest();
	
	request.open("GET", "http://localhost:8080/plants");
	request.send(null);

	
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log(request.responseText);
				console.log(JSON.parse(request.responseText));
				var messages = JSON.parse(request.responseText);
				console.log(messages[0]);
				
				var list = document.getElementById("list");
					list.innerHTML = "";
				
				
				for (i = 0; i < messages.length; i++) { 
    				var text = (messages[i] + "<br>");
			
					var newListItem = document.createElement("li");
					newListItem.innerHTML = text;
			
					var list = document.getElementById("list");
					list.appendChild(newListItem);
		}
		
		
			} else {
				console.error("that didnt work...");
			}
		}
	};
		
};

var getButton = document.getElementById("getButton");
	getButton.onclick = function () {
	console.log("the GET button was clicked!");
	getDataFromServer();
};














