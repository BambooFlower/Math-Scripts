% Steepest descent algorithm
function [x] = SteepestDescent(gfun, ggrad, x0, tau, maxit)
    
    % Init
    x = x0;
    g = gfun(x);
    X = x0; % history of iterates
    % Iterate
    for k=1:maxit
        if (g<tau) % Assume min g(x) = 0
            break
        end
        % Descent direction
        d = -ggrad(x);
        % Line search
        t = fminbnd(@(t)gfun(x + t*d), 0, 100);
        % SD Update
        x = x + t*d;
        g = gfun(x);
        X(:, k+1) = x; % record the new iterate
        fprintf('SD iter %d,\t g(x) = %g\n', k, g);
    end
    
end