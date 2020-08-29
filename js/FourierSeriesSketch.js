var fs = function( p ) {

  let time = 0;
  let wave = [];

  let slider;

  p.setup = function() {
    p.createCanvas(1200, 400);
    slider = p.createSlider(1, 10, 5);
  }

  p.draw = function() {
    p.background(0);
    p.translate(150, 200);

    let x = 0;
    let y = 0;

    for (let i = 0; i < slider.value(); i++) {
      let prevx = x;
      let prevy = y;

      let n = i * 2 + 1;
      let radius = 75 * (4 / (n * p.PI));
      x += radius * p.cos(n * time);
      y += radius * p.sin(n * time);

      p.stroke(255, 100);
      p.noFill();
      p.ellipse(prevx, prevy, radius * 2);

      p.stroke(255);
      p.line(-150,-200,-150,400);
      p.line(900,-200,900,400);
      p.line(-150,-200,900,-200);
      p.line(-150,200,900,200);


      p.line(prevx, prevy, x, y);
    }
    wave.unshift(y);
  
    p.translate(200, 0);
    p.line(x - 200, y, 0, wave[0]);
    p.beginShape();
    p.noFill();
    for (let i = 0; i < wave.length; i++) {
      p.vertex(i, wave[i]);
    }
    p.endShape();

    time += 0.05;

    if (wave.length > 650) {
      wave.pop();
    }
  }

};

// Add canvas into the div
var myp5 = new p5(fs, 'fourier');
