var Coins; 
var Coin1;
var Coin2;
var Coin3;
var Result;
var asciipic;

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min);
}

var FlipCoins = function(){
// Flip Coin 3 = heads, 2 = tails
	Coin1 = getRandomInt(2, 3); 
	Coin2 = getRandomInt(2, 3); 
	Coin3 = getRandomInt(2, 3); 
}

var LineCast = function(){
//This function creates the pictures of lines as broken or unbroken
//and changing or unchanging 

Coins = 3; // # of coins

FlipCoins();
Result = Coin1 + Coin2 + Coin3;

	if (Result == 8) {
		asciipic = '=========';
	}
	else if (Result == 6) {
		asciipic = '====x====';
	}
	else if (Result == 7) {
		asciipic = '===&nbsp;&nbsp;&nbsp;===';
	}
	else if (Result == 9) {
		asciipic = '===&nbsp;o&nbsp;===';
	}

}// End LineCast Function
