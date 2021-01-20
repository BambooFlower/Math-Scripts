% Surface of Revolution Visualization

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
t_L = 0;
t_U = 2*pi;

% Mesh density
Mesh = 50;

% Catenoid Parametrization:
syms u v

x = sin(u)*cos(v);
y = cos(u)*sin(v);
z = sin(u);

% Plotting:
fsurf(x,y,z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Surface of Revolution')
xlabel('X')
ylabel('Y')
zlabel('Z')

