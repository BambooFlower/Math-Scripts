% Helicoid visualization

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
t_L = -1;
t_U = 1;

% Mesh density
Mesh = 50;

% Helicoid Parametrization:
syms u t

x = u*cos(t);
y = u*sin(t);
z = (2/3)*t;

% Plotting:
fsurf(x,y,z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Helicoid')
xlabel('X')
ylabel('Y')
zlabel('Z')