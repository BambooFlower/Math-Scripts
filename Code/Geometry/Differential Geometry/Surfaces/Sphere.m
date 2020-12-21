% Sphere Visualization

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
v_L = -pi;
v_U = pi;

% Mesh density
Mesh = 50;

% Sphere Parametrization:
syms u v

x = sin(u)*cos(v);
y = cos(u)*cos(v);
z = sin(v);

% Plotting:
fsurf(x,y,z,[u_L, u_U, v_L, v_U], 'meshdensity', Mesh)
title('Sphere')
view(40,10);
xlabel('X')
ylabel('Y')
zlabel('Z')
