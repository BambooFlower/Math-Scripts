% Enneper surface visualization

close all 
clear 

% Limits on parameters
u_L = -2*pi;
u_U = 2*pi;
v_L = -2*pi;
v_U = 2*pi;

% Mesh density
Mesh = 50;

% Enneper Surface Parametrization:
syms u v 

x = u*(1-(u^2)/3 + v^2)/3;
y = v*(1-(v^2)/3 + u^2)/3;
z = (u^2 - v^2)/3;

% Plotting:
fsurf(x,y,z,[u_L, u_U, v_L, v_U], 'meshdensity', Mesh)
title('Enneper Surface')
xlabel('X')
ylabel('Y')
zlabel('Z')

