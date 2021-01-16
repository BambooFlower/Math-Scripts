% Pseudosphere visualization

close all 
clear 

% Limits on parameters
u_L = -3;
u_U = 3;
v_L = -pi;
v_U = pi;

% Mesh density
Mesh = 50;

% Pseudosphere Parametrization:
syms u v 

x = sech(u)*cos(v);
y = sech(u)*sin(v);
z = u - tanh(u);

% Plotting:
fsurf(x,y,z,[u_L, u_U, v_L, v_U], 'meshdensity', Mesh)
title('Pseudosphere')
xlabel('X')
ylabel('Y')
zlabel('Z')

