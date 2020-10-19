function [r,v,T] = simpleorbit()
% Circular orbit
% Earth and Sun measurements were used for calculations

close all

% Orbit parameters:
e = 0.0167; % Orbit eccentricity
mu_S = 132712439935.5; % Sun parameter in Km^3/s^2
R_S = 6.957*10^5; % Sun radius in Km
a = 149.6*1e6; % Semimajor axis in Km
theta0  = 0;

% Time
T = 2*pi*sqrt(a^3/mu_S);
tfin = 10*T; % Change the scaling parameter to change the time of the simulation

% Initial Conditions:
rx0 = a*(1-e^2)/(1+e*cos(theta0));
vy0 = sqrt(2*mu_S/rx0-mu_S/a);
X0 = [rx0,0,0,0,vy0,0];
options = odeset('Reltol',1e-15,'AbsTol',1e-15);

% Integration:
[T, X]  = ode113(@dynamics, [0,tfin], X0, options, mu_S);
r = [X(:,1),X(:,2),X(:,3)];
v = [X(:,4),X(:,5),X(:,6)];

% Draw planet
figure
[sx,sy,sz] = sphere(100);
surf(R_S*sx,R_S*sy,R_S*sz,'EdgeColor','none','FaceColor','y')

% Aspect
hold on
axis equal
grid on
axis([-2*a,2*a,-2*a,2*a,-2*R_S,2*R_S])

% Plot:
title('Circular Orbit Around a Star')
comet3(r(:,1),r(:,2),r(:,3))
end

function [dX] = dynamics(~,X,mu)

rx = X(1);
ry = X(2);
rz = X(3);
vx = X(4);
vy = X(5);
vz = X(6);

r  = sqrt(rx.^2+ry.^2+rz.^2);
dX(1,1) = vx;
dX(2,1) = vy;
dX(3,1) = vz;
dX(4,1) = -mu*rx/r.^3;
dX(5,1) = -mu*ry/r.^3;
dX(6,1) = -mu*rz/r.^3;
end



