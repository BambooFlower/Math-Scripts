% Torus Visualization

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
v_L = -pi;
v_U = pi;

% Mesh density
Mesh = 50;

% Torus Parametrization:
syms u v

gamma = pi/2;
x = (3 + (1.5)*cos(u))*sin(v);
y = (3 + (1.5)*cos(u))*cos(v);
z = (1.5)*sin(u);

% Plotting:
fsurf(x,y,z, [u_L, u_U, v_L, v_U],'meshdensity', Mesh)
title('Torus')
view(5,65)
xlabel('X')
ylabel('Y')
zlabel('Z')