function SuperFormula3D(n,a)
    
  close all  
    
  u = -pi:0.05:pi;
  v = -pi/2:0.05:pi/2;
  
  x = zeros(length(u),length(v));
  y = zeros(length(u),length(v));
  z = zeros(length(u),length(v));
  
  nu = length(u);
  nv = length(v);
  for i = 1:nu
    for j = 1:nv
      raux1 = abs(1/a(1)*abs(cos(n(1).*u(i)/4))).^n(3) + abs(1/a(2)*abs(sin(n(1)*u(i)/4))).^n(4);
      r1 = abs(raux1).^(-1/ n(2));
      raux2 = abs(1/a(1)*abs(cos(n(1)*v(j)/4))).^n(3) + abs(1/a(2)*abs(sin(n(1)*v(j)/4))).^n(4);
      r2 = abs(raux2).^(-1/n(2));
      x(i,j) = r1*cos(u(i))*r2*cos(v(j));
      y(i,j) = r1*sin(u(i))*r2*cos(v(j));
      z(i,j) = r2*sin(v(j));
    end
  end
  
  mesh(x, y, z)
  colormap jet
  title('3D Supershape')
  xlabel('X-Axis')
  ylabel('Y-Axis')
  zlabel('Z-Axis')
end


% Example:
% n = [8,0.5;0.5,8]
% a = [1;1]
% SuperFormula3D(n,a)
% Check this Wikipedia page for more examples: https://en.wikipedia.org/wiki/Superformula




