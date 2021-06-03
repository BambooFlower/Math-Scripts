// Recursive implemenation of addition chaining

unsigned long fast_exp(unsigned long x, unsigned long y, unsigned long N) {        
    unsigned long tmp;         
        if(y==1) return(x % N);         
        if ((y&amp1)==0) {               
            tmp = fast_exp(x,y/2,N);               
            return ((tmp* tmp)%N);         
        }         
        else {               
            tmp = fast_exp(x,(y-1)/2,N);               
            tmp = (tmp* tmp)%N;               
            tmp = (tmp* x)%N;               
            return (tmp);         
        }    
}