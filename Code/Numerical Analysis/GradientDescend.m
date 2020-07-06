% Example of Gradient Descent

x = 6.0; % Starting point
step_size = 0.01;
step_tolerance = 0.00001;
max_iterations = 10000;

% Derivative function f'(x)
df = @(x) 4*x^3 - 9*x^2;

% Gradient descent iteration
for j = 0:max_iterations
    step = step_size*df(x);
    x = x - step;

    if abs(step) <= step_tolerance
        break
    end
end

fprintf('Minimum: %.6f\n', x); % 2.249965
fprintf('Exact: %.6f\n', 9/4); % 2.250000
fprintf('Iterations: %d\n', j); % 69