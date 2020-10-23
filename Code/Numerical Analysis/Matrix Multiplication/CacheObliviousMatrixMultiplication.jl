# Compute C = A * B, using a cache-obvious multiplication algorithm

function add_matmul_rec!(m,n,p, i0,j0,k0, C,A,B)
    if m+n+p <= 64   # base case: naive matmult for sufficiently large matrices
        for i = 1:m
            for k = 1:p
                c = zero(eltype(C))
                for j = 1:n
                    @inbounds c += A[i0+i,j0+j] * B[j0+j,k0+k]
                end
                @inbounds C[i0+i,k0+k] += c
            end
        end
    else
        m2 = m ÷ 2; n2 = n ÷ 2; p2 = p ÷ 2
        add_matmul_rec!(m2, n2, p2, i0, j0, k0, C, A, B)
        
        add_matmul_rec!(m-m2, n2, p2, i0+m2, j0, k0, C, A, B)
        add_matmul_rec!(m2, n-n2, p2, i0, j0+n2, k0, C, A, B)
        add_matmul_rec!(m2, n2, p-p2, i0, j0, k0+p2, C, A, B)
        
        add_matmul_rec!(m-m2, n-n2, p2, i0+m2, j0+n2, k0, C, A, B)
        add_matmul_rec!(m2, n-n2, p-p2, i0, j0+n2, k0+p2, C, A, B)
        add_matmul_rec!(m-m2, n2, p-p2, i0+m2, j0, k0+p2, C, A, B)
        
        add_matmul_rec!(m-m2, n-n2, p-p2, i0+m2, j0+n2, k0+p2, C, A, B)
    end
    return C
end

function matmul_rec!(C, A, B)
    m,n = size(A)
    n,p = size(B)
    size(C) == (m,p) || error("incorrect dimensions ", size(C), " ≠ $m × $p")
    fill!(C, 0)
    return add_matmul_rec!(m,n,p, 0,0,0, C,A,B)
end


matmul_rec(A, B) = matmul_rec!(Array{promote_type(eltype(A), eltype(B))}(undef,size(A,1), size(B,2)),A, B)

# Example:
# A = rand(50,60)
# B = rand(60,70)
# matmul_rec(A,B)