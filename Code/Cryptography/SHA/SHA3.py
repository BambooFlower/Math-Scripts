import numpy as np
import consts

RHO_MATRICES = {tuple(np.linalg.matrix_power(np.array([[0,1],[2,3]]), t).dot(np.array([1,0])) % 5): t for t in range(0,24)}
RHO_MATRICES[(0,0)] = -1

def arrTransform1(arr):
    output = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                output[i][j][k] = arr[64*(5*j + i)+k]
    return output

def arrTransform2(arr):
    output = [0]*1600
    for i in range(5):
        for j in range(5):
            for k in range(64):
                output[64*(5*j + i)+k] = arr[i][j][k]
    return output

def theta(A_in):
    A_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                x1 = sum([A_in[i-1][jP][k] for jP in range(5)]) % 2
                x2 = sum([A_in[((i+1) % 5)][jP][k-1] for jP in range(5)]) % 2
                s = x1 + x2 + A_in[i][j][k] % 2
                A_out[i][j][k] = s
    return A_out

#= ain[i][j][k − (t + 1)(t + 2)/2]
rhomatrix=[[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
def rho(A_in):
    A_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                t = RHO_MATRICES[(i,j)]
                b = A_in[i][j][k - rhomatrix[i][j]]
                A_out[i][j][k] = b

    return A_out

# aout[j'][2i′ + 3j′][k] = ain[i′][j′][k]
def pi(A_in):
    A_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out[j][(2*i + 3*j) %5][k] = A_in[i][j][k]
    return A_out

# aout[i][j][k] = ain[i][j][k] ⊕ ( (ain[i + 1][j][k] ⊕ 1)(ain[i + 2][j][k]) )
def chi(A_in):
    A_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                or_one = (A_in[(i + 1)%5][j][k] + 1 )% 2
                or_one_mult = or_one * (A_in[(i + 2)%5][j][k])
                A_out[i][j][k] = (A_in[i][j][k] + or_one_mult) % 2
    return A_out

# aout[i][j][k] = ain[i][j][k] ⊕ bit[i][j][k]
# for 0 ≤ ℓ ≤ 6, we have bit[0][0][2ℓ − 1] = rc[ℓ + 7ir]
def iota(A_in, round):
    # generate rc
    A_out = A_in.copy()
    w=[1,0,0,0,0,0,0,0]
    rc = [w[0]]
    for _ in range(1,168):
        w=[w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[0]+w[4]+w[5]+w[6]];
        rc.append(w[0])

    for l in range(7):
        A_out[0][0][2**l - 1] = (A_out[0][0][2**l - 1] + rc[l + 7*round]) % 2

    return A_out

#  ι ◦ χ ◦ π ◦ ρ ◦ θ
def sha3(A_in):
    roundOut = arrTransform1(A_in)
    for r in range(24):
        roundOut = iota(chi(pi(rho(theta(roundOut)))), r)

    ans = arrTransform2(roundOut)
    return ans

#----------------- TESTING  --------------------
shaIn = [0] * 1600
shaIn[0] = 1; shaIn[1087] = 1

shaOut = sha3(shaIn)
print(shaOut[:16])