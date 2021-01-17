% Trefoil Knot Visualization

close all 
clear 

% Limits on parameters
t_L = 0;
t_U = 8;

% Mesh density
Mesh = 10;

% Catenoid Parametrization:
syms t

x = sin(t) + 2*sin(2*t);
y = cos(t) - 2*cos(2*t);
z = -sin(3*t);

% Plotting:
fsurf(x,y,z,[t_L,t_U], 'meshdensity', Mesh)
title('Trefoil Knot')
xlabel('X')
ylabel('Y')
zlabel('Z')

