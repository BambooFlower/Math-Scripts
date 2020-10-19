% Plots the Characteristics, found when solving PDEs, on two Surfacess

close all

% First Surface
x = linspace(0, 5, 50);
y = linspace(-10, 10, 50);
[X,Y] = meshgrid(x, y);
f = @(X,Y) (3*X+4*Y).^3/64;

figure
S = surf(X,Y,f(X,Y));
set(S, 'EdgeColor', 'none', 'FaceColor', 'interp')

hold on

% Plot the initial condition
plot3(0*y, y, y.^3, 'k', 'LineWidth', 6)
% Plot 10 characteristics
C = linspace(y(1), y(end), 10);

for j = 1:length(C)   
    ys = -4/3*x + C(j);   
    us = f(x, ys);
    % This is a trick in order to kill any lines past the end of the domain   
    us(abs(ys) > 10) = NaN;   
    plot3(x, ys, us, 'k')
end

hold off

axis([0 5 -10 10 -2000 3000])
view([-38 16])
title('Surface and Characteristics for u(x,y) = (3x + 4y)^3', 'FontSize', 16)
xlabel('x', 'FontSize', 16)
ylabel('y', 'FontSize', 16)
zlabel('u', 'FontSize', 16)
set(gcf, 'Color', 'w')

% Second Surface
x = linspace(-1, 0.5, 100);
y = linspace(-0.5, 0.5, 100);
[X,Y] = meshgrid(x, y);
f = @(x,y) exp(-3*x).*y.^3;

figure
S = surf(X,Y,f(X,Y));
set(S, 'EdgeColor', 'none', 'FaceColor', 'interp')

hold on

% Plot the initial condition
plot3(0*y, y, y.^3, 'k', 'LineWidth', 6)
% Plot 10 characteristics
C = linspace(y(1), y(end), 10);

for j = 1:length(C)   
    ys = C(j)*exp(-x);   
    us = f(x, ys);   
    us(abs(ys) > 0.5) = NaN;   
    plot3(x, ys, us, 'k')
end

hold off

axis([-1 0.5 -0.5 0.5 -1 1])
view([-42 35])
xlabel('x', 'FontSize', 16)
ylabel('y', 'FontSize', 16)
zlabel('u', 'FontSize', 16)
title('Surface and Characteristics for u(x,y) = e^{-3x} y^3', 'FontSize', 16)
set(gcf, 'Color', 'w')
    
    
    
    