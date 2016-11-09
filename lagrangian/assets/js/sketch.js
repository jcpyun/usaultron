var red= "#dc3439";
var blue= "#3355d5";
var yellow= "#eeb500";
var green= "#86bd00";

var yoff = 0.0;
var state = false;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(255, 255, 255);
  
  //background(255);

}
function draw() {
  var r = random(0, 255);
  var g = random(0, 255);
  var b = random(0, 255);

  stroke(r, g, b);
  strokeWeight(0.2);
  // noFill();
  fill(20);
  beginShape();

  var xoff = 0;
  var xoff = yoff;
  for (var x = -2; x <= width+4; x += 10) {
    var y = map(noise(xoff, yoff), 0, 1, 1, 500)
    vertex(x, y);
    xoff += 0.04;
  }


  yoff += 0.007;
  vertex(width+4, height+4);
  vertex(0, height+4);
  endShape(CLOSE);

}

