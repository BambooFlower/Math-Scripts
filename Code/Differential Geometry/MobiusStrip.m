
clear 
u = linspace(0,2*pi,100);
v = linspace(-0.5,0.5,100);
[u,v] = meshgrid(u,v);

% Parametrization
x = (1+v.*cos(u/2)).*cos(u);
y = (1+v.*cos(u/2)).*sin(u);
z = v.*sin(u/2);


figure(1)
mesh(x,y,z)
axis off
title("Mobius Strip")


% %Code that works and actually produce a Moebius strip
% syms e r;
% s = cos(e)+r*cos(e/2)*cos(e);
% d = sin(e)+r*cos(e/2)*sin(e);
% f = r*sin(e/2);
% figure(4)
% ezsurf(s,d,f, [0, 2*pi, -0.5, 0.5])



