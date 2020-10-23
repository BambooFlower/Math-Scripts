% Implementation of Euler's method

clear 
clc


% Plotting 
y0 = 1;
t0 = 0;
h = 1; % try: h = 0.01
tn = 4; % equal to: t0 + h*n, with n the number of steps
[t, y] = Euler(t0, y0, h, tn);
plot(t, y, 'b');

% exact solution (y = e^t):
tt = (t0:0.001:tn);
yy = exp(tt);
hold('on')
plot(tt, yy, 'r')
hold('off')
legend('Euler', 'Exact')

function [t, y] = Euler(t0, y0, h, tn)
% Numerical Euler's method
    fprintf('%10s%10s%10s%15s\n', 'i', 'yi', 'ti', 'f(yi,ti)');
    fprintf('%10d%+10.2f%+10.2f%+15.2f\n', 0, y0, t0, f(y0,t0));
    t = (t0:h:tn)';
    y = zeros(size(t));
    y(1) = y0;
    
    for i = 1:1:length(t)-1
        y(i+1) = y(i) + h*f(y(i),t(i));
        fprintf('%10d%+10.2f%+10.2f%+15.2f\n', i, y(i+1), t(i+1), f(y(i+1),t(i+1)));
    end
end

% in this case, f(y,t) = f(y)
function dydt = f(y,t)
% Test function
    dydt = y;
end




