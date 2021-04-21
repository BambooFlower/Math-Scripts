# Accelerated row matrix product

C = zeros(m,p)

for j=1:m
    C[j,:] = BLAS.gemv(’T’,B,A[j,:])
end