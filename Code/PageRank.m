function [PI] = PageRank(A, alpha)
% It computes the importance of a vertex using the PageRank algorithm
% This is an algebraic implementation
% At Google a value of alpha=0.85 is used

n = length(A);
OnesVector = ones(n,1);

% Extract the elements of the main diagonal of A 
% and places them in a diagonal matrix D
x = diag(A);
D = diag(x);

% Performing a left division rather than taking the inverse for effeciency
PI = sparse(D)*((sparse(D)-alpha*A)\OnesVector);

end

% Example:
% PageRank(A, 0.85)
