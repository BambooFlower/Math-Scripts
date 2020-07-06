function output = Adaptsmp(f,a,b,tol,lev,fa,fm,fb)
% Adaptive quadrature using Simpson's rule
%
% Call as ADAPTSMP('f',a,b,tol) to approximate the integral of f(x)
% over the interval a < x < b, attempting to achieve a absolute error
% of at most tol(b-a). The first argument should be a string containing
% the name of a function of one variable. The return value is the
% approximate integral.
%
% The variable lev gives the recursion level (which is used to terminate 
% the program if too many levels are used), and fa, fb, and fm are the 
% values of the integrand at a, b, and (a+b)/2, respectively

% initialization, first call only
if nargin == 4
    lev = 1;
    fa = feval(f,a);
    fm = feval(f,(a+b)/2);
    fb = feval(f,b);
end

% Recursive step
% start by checking for too many levels of recursion; if so
% don't do any more function evaluations, just use the already
% evaluated points and return
if lev > 10
    disp('10 levels of recursion reached. Giving up on this interval.')
    output = (b-a)*(fa+4*fm+fb)/6;
else
    % Divide the interval in half and apply Simpson's rule on each half.
    % As an error estimate for this double Simpson's rule we use 1/15 times
    % the difference between it and the simple Simpson's rule (which is
    % an asymptotically exact error estimate).
    h = b - a;
    flm = feval(f,a+h/4);
    frm = feval(f,b-h/4);
    simpl = h*(fa + 4*flm + fm)/12;
    simpr = h*(fm + 4*frm + fb)/12;
    output = simpl + simpr;
    simp = h*(fa+4*fm+fb)/6;
    err = (output-simp)/15;
    % if tolerance is not satisfied, recursively refine approximation
    if abs(err) > tol*h
        m = (a + b)/2;
        output = Adaptsmp(f,a,m,tol,lev+1,fa,flm,fm) ...
            + Adaptsmp(f,m,b,tol,lev+1,fm,frm,fb);
    end
end

end



