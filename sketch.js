var x = 0;

var opp = 1;

function setup() {
	createCanvas(windowWidth, windowHeight);
}

function draw() {
	background(220);
	fill(random(255),random(255),random(255));
	rect(x, 0, 20, 50);
	x = x + 10 * opp;
	if (x <= 0 || x >= windowWidth - 25) {
		opp = opp * -1;
	}
	

}