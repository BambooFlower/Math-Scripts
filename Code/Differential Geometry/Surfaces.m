% Visualization of Surfaces

close all 
clear 

% Limits on parameters
u_L = 0;
u_U = 2*pi;
t_L = -1;
t_U = 1;

% Mesh density
Mesh = 50;

% Helicoid Equation:
syms u t

x = u*cos(t);
y = u*sin(t);
z = (2/3)*t;

% Helicoid Plotting:
figure(1)
fsurf(x,y,z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Helicoid')
xlabel('X')
ylabel('Y')
zlabel('Z')


% Catenoid Equation:
syms u v

gamma = pi/2;
x = cos(gamma)*sinh(v)*sin(u) + sin(gamma)*cosh(v)*cos(u);
y = -cos(gamma)*sinh(v)*cos(u) + sin(gamma)*cosh(v)*sin(u);
z = u*cos(gamma) + v*sin(gamma);

% Catenoid Plotting:
figure(2)
fsurf(x,y,z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Catenoid')
xlabel('X')
ylabel('Y')
zlabel('Z')


% Mobius Strip Equation:
syms u v

x = cos(u)*(1 + (v/2)*cos(u/2));
y = sin(u)*(1 + (v/2)*cos(u/2));
z = (v/2)*sin(u/2);

% Mobius Strip Plotting:
figure(3)
fsurf(x, y, z,[u_L, u_U, t_L, t_U], 'meshdensity', Mesh)
title('Mobius Strip')
xlabel('X')
ylabel('Y')
zlabel('Z')




