// Iterative implementation of addition chaining

unsigned long qe2(unsigned long x, unsigned long y, unsigned long n) {        
    unsigned long s,t,u;        
    int i;        
    
    s = 1; t = x; u = y;        
    while(u) {                
        if(u&amp1) s = (s* t)%n;                
        u>>=1;                
        t = (t* t)%n;        
    }        
    return(s);    
}