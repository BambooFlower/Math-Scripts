// 3D Knot Visualization


float angle = 0;

ArrayList<PVector> vectors = new ArrayList<PVector>();
// r(beta) = 0.8 + 1.6 * sin(6 * beta)
// theta(beta) = 2 * beta
// phi(beta) = 0.6 * pi * sin(12 * beta)

//x = r * cos(phi) * cos(theta)
//y = r * cos(phi) * sin(theta)
//z = r * sin(phi)


float beta = 0;

void setup() {
  size(700, 600, P3D);
}

void draw() {
  background(0);
  translate(width/2, height/2);
  rotateY(angle);
  angle += 0.01;


  float r = 100*(0.8 + 1.6 * sin(6 * beta));
  float theta = 2 * beta;
  float phi = 0.6 * PI * sin(12 * beta);
  float x = r * cos(phi) * cos(theta);
  float y = r * cos(phi) * sin(theta);
  float z = r * sin(phi);
  stroke(255, r, 255);

  vectors.add(new PVector(x,y,z));


  beta += 0.01;


  noFill();
  stroke(255);
  strokeWeight(8);
  beginShape();
  for (PVector v : vectors) {
    float d = v.mag();
    stroke(255, d, 255);
    vertex(v.x, v.y, v.z);
  }
  endShape();
}