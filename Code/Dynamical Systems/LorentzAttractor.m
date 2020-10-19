% PLotting animation of Lorenz Attractor 

% Solve over time interval [0,100] with initial conditions [1,1,1]
% ''f'' is set of differential equations
% ''a'' is array containing x, y, and z variables
% ''t'' is time variable

clear 
close all

% Lorenz System
sigma = 10;
beta = 8/3;
rho = 28;
f = @(t,a) [-sigma*a(1) + sigma*a(2); rho*a(1) - a(2) - a(1)*a(3); -beta*a(3) + a(1)*a(2)];
% Runge-Kutta 4th/5th order ODE solver
[t,a] = ode45(f,[0 100],[1 1 1]);     

% Force 3D view
view(3)
curve = animatedline('Color', 'b');

% Animated Plot
axis([-20 20 -30 30 0 50])
title('Lorenz Attractor')
xlabel('X')
ylabel('Y')
zlabel('Z')
grid on 

for k = 1:length(a)
    addpoints(curve, a(k,1), a(k,2), a(k,3))
    drawnow
end


