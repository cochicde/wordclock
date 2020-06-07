
function createMatrix(letters) {
  var matrixArea = document.getElementById('matrixArea');
  var table = document.createElement('table');
  table.className = "matrixTable"
  for (var row = 0; row < letters.length; row++) {
    var tr = document.createElement('tr');
    for (var column = 0; column < letters[row].length; column++) {
        var td = document.createElement('td');
        tr.appendChild(td)
        
        var div = document.createElement('div');
		td.appendChild(div)
		div.id = row + " " + column
		div.setAttribute('is_on', '0')
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