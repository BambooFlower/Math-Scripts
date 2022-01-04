%% Initialization and Utility
close all;
clear all;

numSims = 5;            % display five runs
tBounds = [3 7];        % The bounds of t
N      = 1000;          % Compute 1000 grid points
dt     = (tBounds(2) - tBounds(1)) / N ;
y_init = 1;             % Initial y condition 


pd = makedist('Normal',0,sqrt(dt)); % Initialize the probability distribution for our 
                         % random variable with mean 0 and 
                         % stdev of sqrt(dt)

c = [0.7, 1.5, 0.06];   % Theta, Mu, and Sigma, respectively

ts    = linspace(tBounds(1), tBounds(2), N); % From t0-->t1 with N points
ys    = zeros(1,N);     % 1xN Matrix of zeros

ys(1) = y_init;
%% Computing the Process
for j = 1:numSims
    for i = 2:numel(ts)
        t = tBounds(1) + (i-1) .* dt;
        y = ys(i-1);
        mu      = c(1) .* (c(2) - y);
        sigma   = c(3);
        dW      = random(pd);
        
        ys(i) = y + mu .* dt + sigma .* dW;
    end
    figure()
    hold on;
    plot(ts, ys, 'o')
end