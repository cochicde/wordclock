
function createMatrix(letters) {
  var matrixArea = document.getElementById('matrixArea');
  var table = document.createElement('table');
  table.className = "matrixTable"
  for (var row = 0; row < letters.length; row++) {
    var tr = document.createElement('tr');
    for (var column = 0; column < letters[row].length; column++) {
        var td = document.createElement('td');
		tr.appendChild(td)
		td.innerHTML = letters[row][column] 
    }
    table.appendChild(tr);
  }
  matrixArea.appendChild(table)
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