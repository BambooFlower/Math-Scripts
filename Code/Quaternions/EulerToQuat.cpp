EulerToQuat(float roll, float pitch, float yaw, QUAT * quat)
// Convert Euler angles to quaternions

{

float cr, cp, cy, sr, sp, sy, cpcy, spsy;

// Calculate trig identities
cr = cos(roll/2);
cp = cos(pitch/2);
cy = cos(yaw/2);
sr = sin(roll/2);
sp = sin(pitch/2);
sy = sin(yaw/2);

cpcy = cp * cy;
spsy = sp * sy;

quat->w = cr * cpcy + sr * spsy;
quat->x = sr * cpcy - cr * spsy;
quat->y = cr * sp * cy + sr * cp * sy;
quat->z = cr * cp * sy - sr * sp * cy;

}