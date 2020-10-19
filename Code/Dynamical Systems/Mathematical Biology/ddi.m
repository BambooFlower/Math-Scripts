function DDI
% This function is used to check the Turing instability of a PDE
% The eigenvalues are given as a1. 

m = 0;
L=1.0; % we use alpha below to set unstable eigenvalue for L=1!
       % by changing L away from 1 you can shift the eigenvalue out of the
       % turing region.

x = linspace(0,L,100);
t =  linspace(0,25,100);

sol = pdepe(m,@pdex4pde,@pdex4ic,@pdex4bc,x,t);
u1 = sol(:,:,1);
u2 = sol(:,:,2);

figure(1)
surf(x,t,u1)
title('u1(x,t)')
xlabel('Distance x')
ylabel('Time t')
zlabel('Concentration of the first component of u')

figure(2)
surf(x,t,u2)
title('u2(x,t)')
xlabel('Distance x')
ylabel('Time t')
zlabel('Concentration of the second component of u')
end


function [c,f,s] = pdex4pde(~,~,u,DuDx)  % cf. Sheet 7 Ind1
b = .5;
d=12;%d>5.8/b for ddi by CW1(d)

c = [1; 1]; 
f = [1; d] .* DuDx; % 2-component flux

% use alpha to set unstable eigenvalues:
% by 1(c) lambda_c= al (bd-1)/2d = al * 5/24 =: (n pi/L)^2 with L=1

% Try different values to get different patterns
% al= 426;  %~(3*pi)^2*24/5;  
% al= 190;  %~(2*pi)^2*24/5;  
al= 47.5;  %~(1*pi)^2*24/5;  
s = al*[u(1)^2/u(2)-b*u(1); u(1)^2-u(2)]; 
end


function u0 = pdex4ic(x)
u0 = [2;4]+.01*[exp(-80*(x-0.3).^2);exp(-80*(x-0.7).^2);]; 
end


function [pl,ql,pr,qr] = pdex4bc(~,~,~,~,~)
pl = [0; 0]; 
ql = [1; 1]; 
pr = [0; 0]; 
qr = [1; 1]; 
end


