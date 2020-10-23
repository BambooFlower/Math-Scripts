function x = GaussSeidel(A, b, x, iters)
% Equation solver for arbitrary number of equations using Gauss-Seidel
% Variables:
% A: Matrix of coefficients of x 
% b: Vector of entries indepedent of x 
% x: Initial/Final values of the solution
% iters: Number of iterations

    for i = 1:iters
        for j = 1:size(A,1)
            x(j) = (1/A(j,j)) * (b(j) - A(j,:)*x + A(j,j)*x(j));
        end
    end
end

% Example:
% A = [10,-1,2,0;-1,11,-1,3;2,-1,10,-1;0,3,-1,8];
% b = [6; 25; -11; 15];
% x = [0; 0; 0; 0];
% iters = 10

