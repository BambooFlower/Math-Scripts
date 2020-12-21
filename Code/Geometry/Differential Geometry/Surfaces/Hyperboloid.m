% Two-Sheeted Hyperboloid Visualization

close all 
clear 

% Limits on parameters
u_L = -5;
u_U = 5;
v_L = 0;
v_U = pi;

% Mesh density
Mesh = 50;

% Hyperboloid Parametrization:
syms u v

x = (2/3)*sinh(u)*cos(v);
y = (2/3)*sinh(u)*sin(v);
z1 = (1/2)*cosh(u);
z2 = -(1/2)*cosh(u);

% Plotting:
figure
hold on
fsurf(x,y,z1,[u_L, u_U, v_L, v_U], 'meshdensity', Mesh)
fsurf(x,y,z2,[u_L, u_U, v_L, v_U], 'meshdensity', Mesh)
hold off

title('Two-Sheeted Hyperboloid')
grid on
view(45,15);
xlabel('X')
ylabel('Y')
zlabel('Z')
