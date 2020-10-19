#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define TWOPI 6.283185307179586476925287
#define NSEGMENTS 1000
#define RADIUS .50

int main(argc,argv)
int argc;
char **argv;
{
   int i;
   double x,y,z,xlast,ylast,zlast;
   double mu;

   for (i=0;i<=NSEGMENTS;i++) {
      mu = i * TWOPI / (double)NSEGMENTS;
      x = 10 * (cos(mu) + cos(3*mu)) + cos(2*mu) + cos(4*mu);
      y = 6 * sin(mu) + 10 * sin(3*mu);
      z = 4 * sin(3*mu) * sin(5*mu/2) + 4*sin(4*mu) - 2 * sin(6*mu);

      /*
         Write the geometry in any format you like
         Here I create sphere and cylinder combinations for Radiance
      */
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