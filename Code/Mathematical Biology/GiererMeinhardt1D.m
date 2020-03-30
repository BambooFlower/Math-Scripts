% Turing Instabilities: Gierer Meinhardt system in 1D
% This MATLAB code will show a numerical simulation the 1D Gierer Meinhardt system

clear
close all
 
% Parameter values
bc  = 0.35; 
% Diffusion constants
Du = 1;   
Dv = 30;  
 
% Grid and initial data:
% No Pattern 
% w = 10; 
% Pattern
w = 80;  
 
Nx = 500; % How many points we want to discretize our domain with
x = linspace(0,w, Nx); 
dx = x(2) - x(1); 
 
dt = 1; % size of our time step
t = 0:dt:400;   
Nt = length(t); % Number of time points
 
% Set up for the surface 
[X, T] = meshgrid(x, t); 
U = 0*X;
V = 0*X;
 
% Easier to deal with column vectors
x = x(:);
t = t(:);
 
% Initial conditions: small perturbation away from steady state
u = 1/bc*ones(length(x),1) + 0.01*rand(Nx, 1); 
v = 1/bc^2*ones(length(x),1);
 
% Save initial conditions
U(1,:) = u;
V(1,:) = v;
 

% To begin, let us recall how to set up the matrices used in the explicit
% and implicit finite difference methods.
 
 
% Forward (explicit) method 
% We want a tridiagonal matrix (see notes for details) 
a = (1-2*Du*dt/dx^2);  % values along the diagonal
b = Du*dt/dx^2;        % values in the off-diagonal
main = a*sparse(ones(Nx,1)); 
off  = b*sparse(ones(Nx-1,1));
Bu = diag(main) + diag(off,1) + diag(off,-1); %Still a sparse matrix
% Satisfying boundary conditions
Bu(1, end-1) = b; 
Bu(end, 2) = b;
 
% To have a more numerically stable code, we use the implicit method. 
% Backward (implicit) method 
% For u
    a = (1+2*Du*dt/dx^2);  % values along the diagonal
    b = Du*dt/dx^2;        % values in the off-diagonal
    main = a*sparse(ones(Nx,1)); 
    off  = -b*sparse(ones(Nx-1,1));
    Bu = diag(main) + diag(off,1) + diag(off,-1); %Still a sparse matrix
    % Satisfying boundary conditions
    Bu(1, end-1) = -b; 
    Bu(end, 2) = -b;
 
% Same thing for v
    a = (1+2*Dv*dt/dx^2); b = Dv*dt/dx^2;
    main = a*sparse(ones(Nx,1));
    off  = -b*sparse(ones(Nx-1,1));
    Bv = diag(main) + diag(off,1) + diag(off,-1);
    Bv(1, end-1) = -b;
    Bv(end, 2) = -b;

% Plotting 
figure(1)
plot(x,u,'g.-', 'linewidth',1);
hold on;
plot(x,v,'r.-', 'linewidth',1);
hold off;
 
axis([-1 80 -.01 15.01])  
 
for j = 1:Nt
    % f and g are the reaction terms in the G-M system
    f = u.^2./v-bc*u;
    g = u.^2 - v;
 
    % At each step we need to solve the system
    u = Bu\(u + dt*f);   % backward Euler
    v = Bv\(v + dt*g);
 
    % Plot
    plot(x,u,'g.-', 'linewidth',1);
    hold on;
    plot(x,v,'r.-', 'linewidth',1);
    hold off;
    axis([-1 80 -.01 15.01])
    title(['t = ', num2str(j*dt)],'fontsize',24)
    xlabel('Distance x')
    ylabel('Concentration')
    legend('Concentration of u','Concentration of v')
    drawnow; 
 
    % Save for surface
    U(j,:) = u;
    V(j,:) = v;
end
 
 
% Surface Plot
figure(2)
s = surf(x, t, U);
% Set up the colors
set(s, 'EdgeColor', 'none', 'FaceColor', 'interp') 
xlabel('Distance x') 
ylabel('Time t') 
zlabel('Concentration u')
title('Surface plot of the solution of the 1D Gierer Meinhardt system')
 
% Contour plot
figure(3)
p = pcolor(x, t, U);
set(p, 'EdgeColor', 'none', 'FaceColor', 'interp')
xlabel('Distance x')
ylabel('Time t')
title('Contour plot of the solution of the 1D Gierer Meinhardt system')
