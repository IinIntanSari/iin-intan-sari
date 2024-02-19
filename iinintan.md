function setup() {
  createCanvas(400, 400);
  background(255);
}

function draw() {
  translate(width / 2, height / 2);
  drawFlower(0, 0, 10, 100, 4);
}

function drawFlower(x, y, numPetals, petalLength, petalWidth) {
  noStroke();
  fill('pink');
  for (let i = 0; i < numPetals; i++) {
    let angle = TWO_PI / numPetals * i;
    let petalX = cos(angle) * petalLength;
    let petalY = sin(angle) * petalLength;
    ellipse(petalX, petalY, petalWidth, petalLength);
  }
  fill('yellow');
  ellipse(0, 0, petalWidth, petalWidth); // Center of the flower
}
