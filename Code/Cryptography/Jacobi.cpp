/* This algorithm computes the Jacobi symbol recursively */    
int jacobi(int a, int b)

{    
int g;        
    assert(odd(b));        
    if (a >= b) a %= b;              
    if (a == 0) return 0;              
    if (a == 1) return 1;              
    if (a < 0)        
    if (((b-1)/2 % 2 == 0)            
        return jacobi(-a,b);        
    else            
        return -jacobi(-a,b);        
    if (a % 2 == 0)        
    if (((b*b - 1)/8) % 2 == 0)            
        return +jacobi(a/2, b)        
    else            
        return -jacobi(a/2, b)        
    g = gcd(a,b);        
    assert(odd(a));     /* this is guaranteed by the (a % 2 == 0)    test */        
    if (g == a)         /* a exactly divides b */       
    return 0;        
    else if (g != 1)        
    return jacobi(g,b) * jacobi(a/g, b);      
    else if (((a-1)*(b-1)/4) % 2 == 0)        
    return +jacobi(b,a);            
    else        
    return -jacobi(b,a);       
}