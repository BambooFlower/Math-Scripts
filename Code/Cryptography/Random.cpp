// Pseudo-random number generator based on the CPU's counter register

char Randpool[16];
/* Call early and call often on a wide variety of random or semi-random system events to churn the randomness pool. 
* The exact format and length of randevent doesn’t matter as long as its contents are at least somewhat unpredictable. */

void churnrand(char *randevent,unsigned int randlen){     
    MD5_CTX md5;     
    MD5Init(&ampmd5);     
    MD5Update(&ampmd5,Randpool,sizeof(Randpool));     
    MD5Update(&ampmd5,randevent,randlen);     
    MD5Final(Randpool,&ampmd5);
}

long Randcnt;
void genrand(char *buf,unsigned int buflen)
{
    MD5_CTX md5;     
    char tmp[16];     
    unsigned int n;

    while(buflen != 0) {          
        /* Hash the pool with a counter */          
        MD5Init(&ampmd5);          
        MD5Update(&ampmd5,Randpool,sizeof(Randpool));          
        MD5Update(&ampmd5,(unsigned char *)&ampRandcnt,sizeof(Randcnt));          
        MD5Final(tmp,&ampmd5);          
        Randcnt++; /* Increment counter */      

        /* Copy 16 bytes or requested amount, whichever is less, to the user’s buffer */          
        n = (buflen < 16) ? buflen : 16;          
        memcpy(buf,tmp,n);          
        buf += n;          
        buflen -= n;     
    }
}