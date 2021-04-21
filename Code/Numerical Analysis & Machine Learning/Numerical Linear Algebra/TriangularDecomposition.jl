# Triangular decompostion with Partial Pivoting 

p = collect (1:m)                                       # initialization of the permutation vector

for k=1:m
    j = indmax(abs(A[k:m,k])); j = k-1+j                # pivot search
    p[[k,j]] = p[[j,k]]; A[[k,j],:] = A[[j,k],:]        # row swap
    A[k+1:m,k] /= A[k,k]
    A[k+1:m,k+1:m]  -= A[k+1:m,k]*A[k:k,k+1:m]
end