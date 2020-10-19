#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define TWOPI 6.283185307179586476925287
#define NSEGMENTS 1000
#define RADIUS 0.05

int main(argc,argv)
int argc;
char **argv;
{
   int i;
   double x,y,z,xlast,ylast,zlast;
   double mu;
   int nlongitude,nmeridian;

   nmeridian  = atoi(argv[1]);
   nlongitude = atoi(argv[2]);

   for (i=0;i<=NSEGMENTS;i++) {
      mu = i * TWOPI * nmeridian / (double)NSEGMENTS;
      x = cos(mu) * (1 + cos(nlongitude*mu/(double)nmeridian) / 2.0);
      y = sin(mu) * (1 + cos(nlongitude*mu/(double)nmeridian) / 2.0);
      z = sin(nlongitude*mu/(double)nmeridian) / 2.0;

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