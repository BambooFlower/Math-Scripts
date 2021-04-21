# QR-decomposition using the MSG algorithm

R = zeros(n,n) 

for k=1:n
    R[k,k] = norm(A[:,k])
    A[:,k] /= R[k,k]
    R[k:k,k+1:n] = A[:,k]’*A[:,k+1:n]
    A[:,k+1:n]  -= A[:,k]*R[k:k,k+1:n]
end