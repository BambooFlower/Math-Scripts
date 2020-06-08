function film = Graph_Flow_NavierStokes
% This function creates the animation of the solutions

% Loading the data
load('Data_NavierStokes_Flow','nbr','l','L','T','lambda_max',...
    'alpha0','alpha','lambdass','Nss','Pss')

% Building the mesh
x = linspace(0,l,200);
y = linspace(0,L,200);
[X,Y] = meshgrid(x,y);
[nbr_x,nbr_y] = size(X);
nbr_time_step = length(T);
sol = alpha.';

% Initialization
figure(1);
rectangle('Position',[0 0 l L],'linewidth',2)
axis equal
axis([0 l 0 L])
hold on

nbr_tot = nbr_x*nbr_y;
omega = zeros(nbr_tot,nbr);
Xp = reshape(X,nbr_tot,1);
Yp = reshape(Y,nbr_tot,1);
for ind =1:nbr
    n = Nss(ind);
    p = Pss(ind);
    omega(:,ind) = pi^2*(n^2/l^2+p^2/L^2)*sin(pi*n.*Xp./l).*sin(pi*p.*Yp./L)*...
        (2*sqrt(l*L))/(pi*sqrt(n^2*L^2+l^2*p^2));
end

% First time step
t = 1;
omega_t = omega*sol(:,t);
omega_t = reshape(omega_t,nbr_x,nbr_y);
toto = pcolor(X,Y,omega_t);
shading interp
colormap jet
% brighten(-0.3)
title('2D Animation of the Navier-Stokes Equations')
caxis([-6 6])

drawnow
film(1) = getframe;

% Main loop
for t = 2:nbr_time_step
    omega_t = omega*sol(:,t);
    omega_t = reshape(omega_t,nbr_x,nbr_y);
    set(toto,'Xdata',X,'Ydata',Y,'Cdata',omega_t)
    
    drawnow
    
    film(t) = getframe; %#ok<AGROW>
end
