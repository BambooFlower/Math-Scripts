function SuperFormula2D(n,a)
% 2D Supershape plotter
    
  close all
  
  u = 0:.001:2*pi;
  raux = abs(1/a(1).*abs(cos(n(1)*u/4))).^n(3) + abs(1/a(2).*abs(sin(n(1)*u/4))).^n(4);
  r = abs(raux).^(-1/n(2));
  x = r.*cos(u);
  y = r.*sin(u);
  
  plot(x,y)
  title('2D Supershape')
  xlabel('X-Axis')
  ylabel('Y-Axis')
end


% Example:
% n = [16,0.5;0.5,16]
% a = [1;1]
% SuperFormula2D(n,a)
% Check this Wikipedia page for more examples: https://en.wikipedia.org/wiki/Superformula