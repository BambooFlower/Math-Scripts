function [x] = Newton(ffun, Jfun, x0, maxit, tau)
    % Newton method
    % Inputs:
    %   ffun and Jfun are handles of residual and Jacobian functions
    %   x0 is the initial guess
    %   maxit is the maximal number of iterations
    %   tau is the stopping residual tolerance
    % Output:
    %   x is the approximate solution
    
    
    % Init.
    x = x0;
    f = ffun(x);
    res_norm = norm(f); % 2-norm by default
    
    % Iterate
    for k=1:maxit
        if (res_norm<tau)
            break;
        end
        J = Jfun(x);
        
        % Newton update
        x = x - J\f;
        
        % Update the residual
        f = ffun(x);
        res_norm = norm(f);
        fprintf('Newton iter = %d, \t res_norm = %g\n', k, res_norm);
    end
end