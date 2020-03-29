function [K] = KatzCentrality(A, alpha)
% Compute the Katz centrality vector K for a given alpha and A

n = length(A);
I = eye(n);
OnesVector = ones(n,1);

% Performing a left division rather than taking the inverse for effeciency
K = (I-alpha*A)\OnesVector;

end

% Example:
% KatzCentrality(A, 0.1)
