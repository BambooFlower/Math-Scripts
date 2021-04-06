from itertools import combinations

def Simpsons(bases, powers):
    """Find the integers (A, B, C, n) that come closest to solving 
    Fermat's equation, A ** n + B ** n == C ** n 
    Let A, B range over all pairs of bases and n over all powers"""
    equations = ((A, B, iroot(A ** n + B ** n, n), n)
                 for A, B in combinations(bases, 2)
                 for n in powers)
    return min(equations, key=relative_error)

def iroot(i, n): 
    "The integer closest to the nth root of i"
    return int(round(i ** (1./n)))

def relative_error(equation):
    "Error between LHS and RHS of equation, relative to RHS" 
    (A, B, C, n) = equation
    LHS = A ** n + B ** n
    RHS = C ** n
    return abs(LHS - RHS) / RHS




# Examples:
# Simpsons(range(1000, 2000), [11, 12, 13])
# Simpsons(range(3000, 5000), [12])
