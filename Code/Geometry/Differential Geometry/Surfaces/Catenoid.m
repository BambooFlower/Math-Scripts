% Catenoid Visualization

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
t_L = -1;
t_U = 1;

% Mesh density
Mesh = 50;

% Catenoid Parametrization:
syms u v

gamma = pi/2;
x = cos(gamma)*sinh(v)*sin(u) + sin(gamma)*cosh(v)*cos(u);
y = -cos(gamma)*sinh(v)*cos(u) + sin(gamma)*cosh(v)*sin(u);
z = u*cos(gamma) + v*sin(gamma);

% Plotting:
fsurf(x,y,z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Catenoid')
xlabel('X')
ylabel('Y')
zlabel('Z')

