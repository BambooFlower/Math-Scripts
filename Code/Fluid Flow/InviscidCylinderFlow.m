function InviscidCylinderFlow(AsymVelocity)
% Plots Streamlines and Velocity field of an inviscid, incompressible, 
% irrotational flow around a cylinder section (radius = 1)
% Default velocity set to 20
%
% INPUT:
% AsymVelocity  = Asymptotic Velocity 
%
% EXAMPLE:
% CylinderFlow(50)


close all

if nargin == 0
    AsymVelocity = 20;
end

% FIRST PART: Streamlines
%
%
% Radius of the Cylinder
a = 1 ;   
c = -a*2;
b = a*2;
% Number of Intervals
n = a*50; 
% First Mesh
[x,y] = meshgrid((c:(b-c)/n:b),(c:(b-c)/n:b)');

% Scales the Streamlines 
for i=1:length(x)
   for k=1:length(x)
      if sqrt(x(i,k).^2+y(i,k).^2) < a
         x(i,k) = 0;
         y(i,k) = 0;
      end
   end
end

% Definition of Polar Variables based on the First Mesh
rho = sqrt(x.^2+y.^2);
theta = atan2(y,x);

% Creation of the streamline function
z = AsymVelocity.*sin(theta).*rho.*(1-(a^2./(rho.^2)));

% Streamlines Plot 
axis square
contour(x,y,z,15)


% SECOND PART: Velocity Field
%
%
% Creation of vectors around the circle
x = -a*2:a/3:a*2;
% Second Mesh
[x] = meshgrid(x);
y = x';

% Scales the Velocity Field
for i=1:length(x)
   for k=1:length(x)
      if sqrt(x(i,k).^2+y(i,k).^2) < a
         x(i,k) = 0;
         y(i,k) = 0;
      end
   end
end

% Definition of Polar Variables based on the First Mesh
r = sqrt(x.^2+y.^2);
theta = atan2(y,x);

% Laminar Stream Functions in Polar Coordinates
ur = AsymVelocity*cos(theta).*(1-a^2./(r.^2));
ut = -AsymVelocity*sin(theta).*(1+a^2./(r.^2));

% Velocities in x-y Coordinates
u = ur.*cos(theta) - ut.*sin(theta);
v = ur.*sin(theta) + ut.*cos(theta);

% Creating the Filled Circle
t_r  = 0:.1:2*pi;
xxx = a*cos(t_r);
yyy = a*sin(t_r);

% Velocity Vectors Plotting
hold on
quiver(x,y,u,v)

% Creating the Filled Circle
fill(xxx,yyy,'y')
axis square
title('Velocity Vectors & Streamlines of an Inviscid Flow')
xlabel('X-Axis')
ylabel('Y-Axis')


end


