MatToQuat(float m[4][4], QUAT * quat)
// Convert a rotation matrix to quatornions

{
    float  tr, s, q[4];
    int    i, j, k;
    int nxt[3] = {1, 2, 0};
    tr = m[0][0] + m[1][1] + m[2][2];

    // check the diagonal
    if (tr > 0.0) {
        s = sqrt (tr + 1.0);
        quat->w = s / 2.0;
        s = 0.5 / s;
        quat->x = (m[1][2] - m[2][1]) * s;
        quat->y = (m[2][0] - m[0][2]) * s;
        quat->z = (m[0][1] - m[1][0]) * s;

    } else {		
        // diagonal is negative
        i = 0;

        if (m[1][1] > m[0][0]) i = 1;
        if (m[2][2] > m[i][i]) i = 2;

        j = nxt[i];
        k = nxt[j];
        s = sqrt ((m[i][i] - (m[j][j] + m[k][k])) + 1.0);
        q[i] = s * 0.5;

        if (s != 0.0) s = 0.5 / s;

        q[3] = (m[j][k] - m[k][j]) * s;
        q[j] = (m[i][j] + m[j][i]) * s;
        q[k] = (m[i][k] + m[k][i]) * s;

        quat->x = q[0];
        quat->y = q[1];
        quat->z = q[2];
        quat->w = q[3];
    }
}