var Marbles; 
var Chosen;
var asciipic;

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * max + min); 
}

var PickMarble = function(Marbles){
// Select a Marble

	Chosen = getRandomInt(1, Marbles); 
}

var LineCast = function(){
//This function creates the pictures of lines as broken or unbroken
//and changing or unchanging 

Marbles = 38; // # of marbles in the bag

PickMarble(Marbles);

	if (Chosen <= 11) {
		asciipic = '=========';
	}
	else if (Chosen <= 19) {
		asciipic = '====x====';
	}
	else if (Chosen <= 36) {
		asciipic = '===&nbsp;&nbsp;&nbsp;===';
	}
	else if (Chosen <= 38) {
		asciipic = '===&nbsp;o&nbsp;===';
	}

}// End LineCast Function

