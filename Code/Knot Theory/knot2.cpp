#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define PI 3.141592653589793238462643
#define TWOPI 6.283185307179586476925287
#define NSEGMENTS 1000
#define RADIUS 0.1

int main(argc,argv)
int argc;
char **argv;
{
   int i;
   double x,y,z,xlast,ylast,zlast;
   double mu;

   for (i=0;i<=NSEGMENTS;i++) {
      mu = i * TWOPI / (double)NSEGMENTS;
      x = (4 * cos(mu + PI)) / 3 + 2 * cos(3 * mu);
      y = 4 * sin(mu) / 3 + 2 * sin(3 * mu);
      z = sin(4 * mu) + sin(2 * mu) / 2;

      if (i < NSEGMENTS)
         printf("surf sphere s%d\n0 0 4 %g %g %g %g\n",i,x,y,z,RADIUS);
      if (i != 0)
         printf("surf cylinder c%d\n 0 0 7 %g %g %g %g %g %g %g\n",
            i,xlast,ylast,zlast,x,y,z,RADIUS);
      xlast = x;
      ylast = y;
      zlast = z;
   }
}