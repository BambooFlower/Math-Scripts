function [x, RelRes, diffX] = GaussSeidel (A, b, x0, tau, m)
% defining the splitting of A
D = diag(diag(A));
E = -tril(A,-1);
F = -triu(A,1);
P = D - E;

% allocating memory for the quantity to be computed
RelRes = zeros(m,1);
diffX = zeros(m,1);
% RelErr = zeros(m,1);

% initialising the method
nb = norm(b);
x = x0;
relres = norm(b - A*x)/nb;
itc = 0;
xprev = x0;

while (relres > tau) && (itc < m) % stopping criteria
    % main iteration
    x = F*x + b;
    x = P\x;
    itc = itc + 1;
    
    % storing the quantities to be given as an output
    relres = norm(b - A*x)/nb;
    RelRes(itc) = relres;
    diffX(itc) = norm(x-xprev)/norm(x);
%     RelErr(itc) = norm(x-xex)/norm(xex);
    xprev = x;
end

% shrink the output to the actual number of iterations carried out
RelRes = RelRes(1:itc);
diffX = diffX(1:itc);

