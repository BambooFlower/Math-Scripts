# Accelerated inner product 

C = zeros(m,p)

for j=1:m
    for l=1:p
        C[j,l] = dot(conj(view(A,j,:)),view(B,:,l))
    end
end