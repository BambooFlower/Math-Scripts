var attract_force = function( p ){
	var attractors = [];
	var particles = [];
	
	p.setup = function() {
		p.createCanvas(400, 400);

		// for (var i = 0; i < 10; i++) {
		//   attractors.push(createVector(random(width), random(height)));
		// }		 
	};
  
	p.mousePressed = function() {
		attractors.push(p.createVector(p.mouseX, p.mouseY));
	};
	
	p.draw = function() {
		p.background(0);
		p.stroke(255);
		p.line(0,0,0,400)
		p.line(0,0,400,0)
		p.line(400,0,400,400)
		p.line(0,400,400,400)
		p.strokeWeight(4);
		particles.push(new ForcesParticle(p.random(p.width), p.random(p.height),p));

		if (particles.length > 100) {
			particles.splice(0, 1);
		}

		for (var i = 0; i < attractors.length; i++) {
			p.stroke(0, 255, 0);
			p.point(attractors[i].x, attractors[i].y);
		}
		for (var i = 0; i < particles.length; i++) {
			var particle = particles[i];
			for (var j = 0; j < attractors.length; j++) {
			  particle.attracted(attractors[j]);
			}
			particle.update();
			particle.show();
		}
  };
}


// Add canvas into the div
var myforce = new p5(attract_force, 'attractrion-repulsion');

