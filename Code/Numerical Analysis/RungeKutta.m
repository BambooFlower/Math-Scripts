% Runge-Kurra fourth order method for numerical ODE solutions
% In this example we use the ODE dy/dx = y*cos(x) to check that the error
% is order h^4

clear
close all

nmat = [50 100 200 400];
f = @(x,y) y*cos(x);
g = @(x) exp(sin(x));

% A nice, fine mesh
xfine = linspace(0, 6*pi, 100);  

figure(1)
plot(xfine, g(xfine), 'rs-')
hold on

for j = 1:length(nmat)    
    tic    
    n = nmat(j);  
    
    x = linspace(0, 6*pi, n);
    % Discretization size 
    h = x(2) - x(1);  
    
    % Initial value
    y(1) = 1;                   
    
    for k = 2:n
        k1 = f(x(k-1), y(k-1));
        k2 = f(x(k-1) + h/2, y(k-1) + h/2*k1);
        k3 = f(x(k-1) + h/2, y(k-1) + h/2*k2);
        k4 = f(x(k-1) + h, y(k-1) + h*k3);
        
        y(k) = y(k-1) + h/6*(k1 + 2*k2 + 2*k3 + k4);
    end
    
    plot(x, y, 'b')
    drawnow
    
    err(j) = norm(g(x) - y, inf);   
    disp(['When n = ', num2str(n), ' the error is ', num2str(err(j))]); 
    
    time(j) = toc;
end

hold off
xlabel('x', 'FontSize', 16)
ylabel('y', 'FontSize', 16)
title('Solution of dy/dx = y cos(x)', 'Fontsize', 16)


