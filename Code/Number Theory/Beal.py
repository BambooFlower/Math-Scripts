from math      import gcd, log
from itertools import combinations, product

def beal(max_A, max_x):
    """See if any A ** x + B ** y equals some C ** z, with gcd(A, B) == 1.
    Consider any 1 <= A,B <= max_A and x,y <= max_x, with x,y prime or 4"""

    
    Apowers = make_Apowers(max_A, max_x)
    Czroots = make_Czroots(Apowers)
    
    for (A, B) in combinations(Apowers, 2):
        if gcd(A, B) == 1:
            for (Ax, By) in product(Apowers[A], Apowers[B]):       
                Cz = Ax + By
                if Cz in Czroots:
                    C = Czroots[Cz]
                    x, y, z = exponent(Ax, A), exponent(By, B), exponent(Cz, C)
                    print('{} ** {} + {} ** {} == {} ** {} == {}'
                          .format(A, x, B, y, C, z, C ** z))

def make_Apowers(max_A, max_x): 
    "A dictionary of {A: [A**3, A**4, ...], ...}"
    
    exponents = exponents_upto(max_x)
    return {A: [A ** x for x in (exponents if (A != 1) else [3])]
            for A in range(1, max_A+1)}

def make_Czroots(Apowers): 
    return {Cz: C for C in Apowers for Cz in Apowers[C]}            
    
def exponents_upto(max_x):
    "Return all odd primes up to max_x, as well as 4"
    
    exponents = [3, 4] if max_x >= 4 else [3] if max_x == 3 else []
    
    for x in range(5, max_x, 2):
        if not any(x % p == 0 for p in exponents):
            exponents.append(x)
            
    return exponents

def exponent(Cz, C): 
    """Recover z such that C ** z == Cz (or equivalently z = log Cz base C).
    For exponent(1, 1), arbitrarily choose to return 3"""
    
    return 3 if (Cz == C == 1) else int(round(log(Cz, C)))





# Example:
# beal(100,100)
