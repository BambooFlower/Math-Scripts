# Compute C = A * B, using naive matrix-multiplication algorithm,
# with a pre-allocated output array C.  ("!" is a Julia convention
# for functions that modify their arguments.)

function matmul!(C, A, B)
    m,n = size(A)
    n,p = size(B)
    size(C) == (m,p) || error("incorrect dimensions ", size(C), " ≠ $m × $p")
    for i = 1:m
        for k = 1:p
            c = zero(eltype(C))
            for j = 1:n
                @inbounds c += A[i,j] * B[j,k]
            end
            @inbounds C[i,k] = c
        end
    end
    return C
end

# a wrapper that allocates C of an appropriate type
matmul(A, B) = matmul!(Array{promote_type(eltype(A), eltype(B))}(undef,size(A,1), size(B,2)),A, B)

# Example:
# A = rand(5,6)
# B = rand(6,7)
# matmul(A,B)