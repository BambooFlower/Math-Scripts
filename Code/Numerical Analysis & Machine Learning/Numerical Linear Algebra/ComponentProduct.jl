# Accelerated component-wise product

C = zeros(m,p)

for j=1:m
    for l=1:p
        for k=1:n
            @inbounds C[j,l] += A[j,k]*B[k,l]
        end
    end
end