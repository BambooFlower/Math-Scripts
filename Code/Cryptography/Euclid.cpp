// Implementation of Euclid's algorithm

/* returns the gcd of x1, x2...xm */    
int multiple_gcd (int m, int *x)    
{         
    size_t i;         
    int g;   

    if (m < 1)               
        return 0;

    g = x[0];         
    for (i=1; i<m; ++i) {               
        g = gcd(g, x[i]);    
    /* optimization, since for random x[i], g==1 60% of the time: */                
        if (g == 1)                     
            return 1;         
    }
    return g;    
}