function [output] = GenFun(A)
% Computes the Walk Generating Function for an adjacency matrix A

I = eye(length(A));

syms x;
output = inv(I-x*A);

end

% Example:
% A = [0,1,0,1;1,0,2,1;0,2,0,0;1,1,0,0];