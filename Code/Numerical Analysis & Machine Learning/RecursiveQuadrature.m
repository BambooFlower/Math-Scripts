function [Q, count] = RecursiveQuadrature(fun, a, b, tol, count)
% Recursive adaptive quadrature that returns also function count, which
% should be initialised to 0 in the first call
%
% Note: only a local estimate of the error is ensured

h = (b-a);
m = (a+b)/2;

% Evaluate the function and count the number of calls
fa = fun(a);
fb = fun(b);
fm = fun(m);
count = count + 3;

% Two quadratures
T = (h/2)*(fa + fb);
S = (h/6)*(fa + 4*fm + fb);

% Estimate the error between them
if  (abs(T-S) >= tol)
    [Q1, count] = RecursiveQuadrature(fun, a, m, tol, count);
    [Q2, count] = RecursiveQuadrature(fun, m, b, tol, count);
    Q = Q1 + Q2;
else 
    Q = S;
end

end
