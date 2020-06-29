QuatToMatrix(QUAT * quat, float m[4][4]){
// Convert Quaternions into a rotation matrix 

    float wx, wy, wz, xx, yy, yz, xy, xz, zz, x2, y2, z2;


    // calculate coefficients
    x2 = quat->x + quat->x; y2 = quat->y + quat->y;
    z2 = quat->z + quat->z;
    xx = quat->x * x2; xy = quat->x * y2; xz = quat->x * z2;
    yy = quat->y * y2; yz = quat->y * z2; zz = quat->z * z2;
    wx = quat->w * x2; wy = quat->w * y2; wz = quat->w * z2;


    m[0][0] = 1.0 - (yy + zz); m[1][0] = xy - wz;
    m[2][0] = xz + wy; m[3][0] = 0.0;

    m[0][1] = xy + wz; m[1][1] = 1.0 - (xx + zz);
    m[2][1] = yz - wx; m[3][1] = 0.0;


    m[0][2] = xz - wy; m[1][2] = yz + wx;
    m[2][2] = 1.0 - (xx + yy); m[3][2] = 0.0;


    m[0][3] = 0; m[1][3] = 0;
    m[2][3] = 0; m[3][3] = 1;

}