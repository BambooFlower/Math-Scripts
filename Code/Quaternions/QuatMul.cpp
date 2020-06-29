QuatMul(QUAT *q1, QUAT *q2, QUAT *res)
// Efficient quaternions multiplication

{
    float A, B, C, D, E, F, G, H;

    A = (q1->w + q1->x)*(q2->w + q2->x);
    B = (q1->z - q1->y)*(q2->y - q2->z);
    C = (q1->w - q1->x)*(q2->y + q2->z); 
    D = (q1->y + q1->z)*(q2->w - q2->x);
    E = (q1->x + q1->z)*(q2->x + q2->y);
    F = (q1->x - q1->z)*(q2->x - q2->y);
    G = (q1->w + q1->y)*(q2->w - q2->z);
    H = (q1->w - q1->y)*(q2->w + q2->z);

    res->w = B + (-E - F + G + H) /2;
    res->x = A - (E + F + G + H)/2; 
    res->y = C + (E - F + G - H)/2; 
    res->z = D + (E - F - G + H)/2;
}