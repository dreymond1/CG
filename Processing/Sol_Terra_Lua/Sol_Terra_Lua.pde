void setup() {
  size(800, 800);
  ellipseMode(CENTER);
}

void draw() {
  background(100);
  translate(width/2, height/2);
  
  pushMatrix();
  fill(242, 204, 47, 250);
  circle(0, 0, 200);
  
  popMatrix();
  
  pushMatrix();
  
  rotate(frameCount/(20*TWO_PI));
  translate(1.4*width/4, 0);
  fill(116, 193, 206, 250);
  circle(0, 0, 50);
  rotate(frameCount/(30*TWO_PI));
  
  pushMatrix();
  
  translate(0.38*width/4, 0);
  fill(255, 255, 255, 250);
  circle(0, 0, 20);
  
  popMatrix();
  
  popMatrix();
}
