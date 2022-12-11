var Marbles; 
var Chosen;
var asciipic;

var HandPile =0 ;
var EastPile = 0;
var WestPile = 0;
var EastRemainder = 0;
var WestRemainder =0 ;
var CountValue1 = 0;
var CountValue2 =0 ;
var CountValue3 = 0;
var LineValue =0 ;

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max) + min); //The maximum is exclusive and the minimum is inclusive
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

	$('Chosen ' + Chosen);
	if (Chosen <= 11) {
		DrawLine('yang',false);
	}
	else if (Chosen <= 19) {
		DrawLine('yang',true);
	}
	else if (Chosen <= 36) {
		DrawLine('yin',false);
	}
	else if (Chosen <= 38) {
		DrawLine('yin',true);
	}

}// End LineCast Function

var DrawLine = function(line,changing){
if (changing && line == 'yin') asciipic = '===&nbsp;o&nbsp;===';
if (changing && line == 'yang') asciipic = '====x====';
if (!changing && line == 'yang') asciipic = '=========';
if (!changing && line == 'yin') asciipic = '===&nbsp;&nbsp;&nbsp;===';
}
