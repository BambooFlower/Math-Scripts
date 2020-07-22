var raycasting = function( p ) { // p could be any variable name
  let walls = [];
  let ray;
  let particle;
  let xoff = 0;
  let yoff = 10000;
  
  p.setup = function() {
	
	
  p.createCanvas(500, 500);
  for (let i = 0; i < 5; i++) {
    let x1 = p.random(p.width);
    let x2 = p.random(p.width);
    let y1 = p.random(p.height);
    let y2 = p.random(p.height);
    walls[i] = new Boundary(x1, y1, x2, y2,p);
  }
  walls.push(new Boundary(0, 0, p.width, 0,p));
  walls.push(new Boundary(p.width, 0, p.width, p.height,p));
  walls.push(new Boundary(p.width, p.height, 0, p.height,p));
  walls.push(new Boundary(0, p.height, 0, 0,p));
  particle = new Particle(p);
	
  };

  p.draw = function() {
  p.background(0);
  for (let wall of walls) {
    wall.show(p);
  }

  particle.update(p.mouseX, p.mouseY)
  particle.show(p);
  particle.look(walls);

  xoff += 0.01;
  yoff += 0.01;
  };
};

// Add canvas into the div
var myp5 = new p5(raycasting, 'First');