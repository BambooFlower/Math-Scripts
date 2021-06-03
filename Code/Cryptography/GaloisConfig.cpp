// Implementation of Galois configuration
// Also known as Galois Linear Feedback Shift Register (LFSR)

#define mask 0×80000057

static unsigned long ShiftRegister=1;
void seed_LFSR (unsigned long seed)
{     
    if (seed == 0) /* avoid calamity */          
        seed = 1;     
    ShiftRegister = seed;
}

int modified_LFSR (void)
{     
    if (ShiftRegister & 0×00000001) {          
        ShiftRegister = ((ShiftRegister ^ mask >> 1) | 0×8000000;          
        return 1;     
    } else {          
        ShiftRegister >>= 1;          
        return 0;     
    }
}