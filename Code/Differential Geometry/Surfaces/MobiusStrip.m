% Mobius Strip Visualization 

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
t_L = -1;
t_U = 1;

% Mesh density
Mesh = 50;

% Mobius Strip Parametrization:
syms u v

x = cos(u)*(1 + (v/2)*cos(u/2));
y = sin(u)*(1 + (v/2)*cos(u/2));
z = (v/2)*sin(u/2);

% Plotting:
fsurf(x, y, z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Mobius Strip')
xlabel('X')
ylabel('Y')
zlabel('Z')

