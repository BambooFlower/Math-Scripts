function H = Hashimoto(A)
% Compute the Hashimoto non-backtracking matrix from the adjacency matrix A

I = full(incidence(digraph(A)));
H = double(I>0)'*double(I<0);
end