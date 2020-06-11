
function createMatrix(letters) {
  var matrixArea = document.getElementById('matrixArea');
  var table = document.createElement('table');
  table.className = "matrixTable"
  table.id = "matrixTable"
  for (var row = 0; row < letters.length; row++) {
    var tr = document.createElement('tr');
    for (var column = 0; column < letters[row].length; column++) {
        var td = document.createElement('td');
        tr.appendChild(td)
        
        var div = document.createElement('div');
		td.appendChild(div)
		div.id = row + " " + column
		div.setAttribute('is_on', '0')
		div.style.background = '#000000'
		div.onclick = function(){
			var rowAndColumn = this.id.split(" ")
			var color = null
			if (this.getAttribute('is_on') == '0'){
				var colorElement = document.getElementById("matrixColor")
				color = colorElement.value	
				this.setAttribute('is_on', '1')
			} else {
				color = '#000000'
				this.setAttribute('is_on', '0')
			}
			this.style.background =  color
			changeColor(rowAndColumn[0], rowAndColumn[1], color.slice(1))
		}
		div.innerHTML = letters[row][column] 
    }
    table.appendChild(tr);
  }
  var colorElement = document.getElementById("matrixColor")
  matrixArea.insertBefore(table, colorElement)
  window.setInterval(getMatrixState, 1000);
}

function getMatrixState(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			var jsonText = JSON.parse(this.responseText)
			var leds = jsonText["leds"]

			for (var led = 0; led < leds.length; led++) {
				var id = leds[led]["row"] + " " + leds[led]["column"]
				cell = document.getElementById(id)
				cell.style.background = 'rgb(' + leds[led]["color"] + ')'
			}
		}
	};
	xhttp.open("GET", "state", true);
	xhttp.send("");
}

function changeColor(row, column, color){
	var xhttp = new XMLHttpRequest();
	path = "/turn_on/" + row + "/" + column + "/" + color
	xhttp.open("POST", path, true);
	xhttp.send("");
}

function setSameHeight(elementId) {
	var element = document.getElementById(elementId);
	var tallestHeight = 0
	for (var child = 0; child < element.children.length; child++) {
		if (element.children[child].offsetHeight > tallestHeight){
			tallestHeight = element.children[child].offsetHeight
		}
	}
	for (var child = 0; child < element.children.length; child++) {
		element.children[child].style.height = tallestHeight  + "px"
	}
}

function createMatrixState(color){
	var jsonState = "{\"leds\":[" 
	var cells = document.getElementById("matrixTable").getElementsByTagName('div')
	for (var divChild = 0; divChild < cells.length; divChild++) {
		var colorToUse = ""
		var rowAndColumn = cells[divChild].id.split(" ")
		if (color == ""){
			colorToUse = cells[divChild].style.backgroundColor.slice(4, -1)
		} else {
			colorToUse = color
		}
		jsonState += "{ \"row\":" + rowAndColumn[0] + ", \"column\":" + rowAndColumn[1] + ", \"color\": \"" + colorToUse + "\"}"
		if (divChild != cells.length - 1) {
			jsonState += ","
		}
	}
	jsonState += "]}"
	return jsonState 
}

function saveState(){
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "/turn_on/", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	xhttp.send(createMatrixState(""));
}

function clearMatrix(){
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "/turn_on/", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	xhttp.send(createMatrixState("0, 0, 0"));
}

function changeClockState(){
	var checkBox = document.getElementById("pauseClock");
	var xhttp = new XMLHttpRequest();
	var path = "/clockState/"
	if (checkBox.checked == true){
		path += 1
	  } else {
		  path += 0
	  }
	xhttp.open("POST", path, true);
	xhttp.send("");
}