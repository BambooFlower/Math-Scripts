#define WIN32_LEAN_AND_MEAN	
#include <windows.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <gl/glut.h>
#include <gl/glu.h>
#include <gl/gl.h>

#ifdef __BORLANDC__
 #include <float.h>
#endif


#define WIDTH 640
#define HEIGHT 540

const double PI = 4*atan(1);
const double PI2 = 2*PI;
const double PI_2 = PI/2;

typedef struct __POS {
	double x,y,z;
} POS;

float lp[3];
float ambientLight[] = { 0.7f, 0.2, 0.2f, 1.0f };
float diffuseLight[] = { 0.9f, 0.6f, 0.6f, 1.0f };
float specularLight[] = { 1.0f, 0.1f, 0.1f, 1.0f };
float ambientLight2[] = { 0.8f, 0.3f, 0.3f, 1.0f };
float diffuseLight2[] = { 0.7f, 0.2f, 0.2f, 1.0f };
float specularLight2[] = { 1.0f, 0.8f, 0.8f, 1.0f };

//rotation angle
int alfa = 0;

//planes count and number of points in each layer
#define LAYERS          40
#define POINTS_IN_LAYER 200

//heart surface constrains
#define        XMIN  -3
#define        XMAX   3
#define        YMIN   XMIN
#define        YMAX   XMAX
#define        ZMIN   XMIN
#define        ZMAX   XMAX
#define        XSIZE  100
#define        YSIZE  XSIZE

POS **heart;

void set( POS &v, double x, double y, double z ) { v.x = x; v.y = y; v.z = z; };

POS cross( POS v1, POS v2 )
{
	POS v;
	v.x = v1.y * v2.z - v1.z * v2.y;
	v.y = v1.z * v2.x - v1.x * v2.z;
	v.z = v1.x * v2.y - v1.y * v2.x;
	return v;
};

POS sub( POS v1, POS v2 )
{
	POS v;
	v.x = v1.x - v2.x;
	v.y = v1.y - v2.y;
	v.z = v1.z - v2.z;
	return v;
}

//heart function : ( 2x^2 + y^2 + z^2 - 1)^3 - 0.1x^2z^3 - y^2z^3
double f( double x,double y,double z )
{
 double xx = x*x;
 double yy = y*y;
 double zz = z*z;
 double a = 2*xx + yy +zz - 1;
 a = a*a*a;
 zz *= z;
 return a - 0.1*xx*zz - yy*zz;
};

//generate points
void initHeart2()
{
  POS    p1, p2, pn;
  double lX,lY,lZ,
	 alfa,
	 dalfa,
	 f1,f2,fn;
  bool finished = false;
  int  i,j,k;

 alfa = 0;
 dalfa = PI2/(double)POINTS_IN_LAYER;


 double X = -1.05;
 int hi = 0;
 double dx = ( 0.70 ) / (double)LAYERS;

 for ( X=-0.70, hi=0; hi<=LAYERS; X+=dx, hi++ ) // first loop
 {
 heart[ hi ]  = (POS*)calloc( POINTS_IN_LAYER, sizeof(POS) );
 POS* h = heart[ hi ];

  for ( i=0; i<POINTS_IN_LAYER; i++ ) //second loop
  {
    alfa = /*PI_2 + */dalfa * i;
    set( p1,X, 0, 0 );
	set( p2,X, cos( alfa ) * YMAX, sin( alfa ) * ZMAX );
    f1 = f( X, p1.y, p1.z );
    f2 = f( X, p2.y, p2.z );
    finished = !( ( f1<=0 ) && ( f2>0 ) );
        while ( !finished )
	{
           pn.y = (p1.y + p2.y) / 2;
           pn.z = (p1.z + p2.z) / 2;
           fn = f( X, pn.y, pn.z );
                if ( fn<=0 )
		{
                   p1 = pn;
                   f1 = fn;
		} else
                      {
                          p2 = pn;
                          f2 = fn;
                      };

           finished = !( ( f1<=0 ) && ( f2>0 ) );
           lY = p2.y - p1.y;
           lZ = p2.z - p1.z;
                if ( sqrt( lZ*lZ + lY*lY ) < 0.001 ) finished = true;
	};

   lY = (p2.y + p1.y)/2;
   lZ = (p2.z + p1.z)/2;
   set( *h, X, lY, lZ );
   h++;
  }; //second loop
 }; //first loop
 
};

void renderScene()
{
 glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
 glPushMatrix();
 glLoadIdentity();
 glRotatef(alfa/10, 0, 1, 0 );
 glScalef( 0.6, 0.6, 0.6 );

 glRotatef( -90, 1, 0, 0);

 POS p[4], n, *h;
 int j,i;

 //draw heart
  for ( j=1; j<=LAYERS; j++ )
	for ( h = heart[ j ], i=0; i<POINTS_IN_LAYER; i++ )
	{
		p[3] = heart[j][i];
		p[2] = heart[j-1][i];
		p[1] = heart[j-1][ (i+1<POINTS_IN_LAYER) ? i+1 : 0 ];
		p[0] = heart[j][ (i+1<POINTS_IN_LAYER) ? i+1 : 0 ];
                n = cross( sub( p[3], p[0] ), sub( p[1], p[0] ) );

          		glFrontFace( GL_CCW );
			 glBegin(GL_POLYGON);
			  glNormal3f( n.x, n.y, n.z );
			   glVertex3f( p[0].x, p[0].y, p[0].z );
			   glVertex3f( p[1].x, p[1].y, p[1].z );
        		   glVertex3f( p[2].x, p[2].y, p[2].z );
			   glVertex3f( p[3].x, p[3].y, p[3].z );
			glEnd();

			glPushMatrix();
			 glScalef(-1,1,1);
                         glFrontFace( GL_CW );
			        glBegin(GL_POLYGON);
        			   glNormal3f( n.x, n.y, n.z );
        			    glVertex3f( p[0].x, p[0].y, p[0].z );
        			    glVertex3f( p[1].x, p[1].y, p[1].z );
        			    glVertex3f( p[2].x, p[2].y, p[2].z );
        			    glVertex3f( p[3].x, p[3].y, p[3].z );
                               glEnd();
        		glPopMatrix();
	};

  //closing polygons
  h = heart[1];

   glFrontFace( GL_CCW );
   glBegin(GL_POLYGON);
    glNormal3f(-1,0,0);
       for ( int i=0; i<POINTS_IN_LAYER; i++ )
        glVertex3f( h[i].x, h[i].y, h[i].z );
   glEnd();

   glPushMatrix();
    glScalef(-1,1,1);
     glFrontFace( GL_CW );

      glBegin(GL_POLYGON);
       glNormal3f(-1,0,0);
          for ( int i=0; i<POINTS_IN_LAYER; i++ )
	   glVertex3f( h[i].x, h[i].y, h[i].z );
      glEnd();

   glPopMatrix();

 glPopMatrix();
 glFlush();
 glutSwapBuffers();

 alfa += 30;
};


int main( int argc, char *argv[] )
{
                #ifdef __BORLANDC__
                 _control87( MCW_EM, MCW_EM ); //fix borlands OGL lighting error
                #endif

	glutInit( &argc, argv );
	glutInitDisplayMode( GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB );
	glutInitWindowPosition( 100, 100 );
	glutInitWindowSize( WIDTH, HEIGHT );
	glutCreateWindow("heart surface");
	glutDisplayFunc(renderScene);
	glutIdleFunc(renderScene);

        glClearColor(.0, .0, .0, 1);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
        glEnable(GL_CULL_FACE);
		glFrontFace( GL_CCW );

        glEnable(GL_LIGHTING);


        glShadeModel(GL_SMOOTH);


	glLightfv(GL_LIGHT2, GL_AMBIENT, ambientLight2);
	glLightfv(GL_LIGHT2, GL_DIFFUSE, diffuseLight2);
        glLightfv(GL_LIGHT2, GL_SPECULAR, specularLight2 );

	glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight);
        glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight );

        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 20.0 );
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 80.0f );

        glEnable(GL_LIGHT2);
        glEnable(GL_LIGHT0);

		float p1[] = { 0,-3,0 };
		glLightfv( GL_LIGHT0, GL_POSITION, p1 );
		float p2[] = { -0,0,-6 };
		glLightfv( GL_LIGHT2, GL_POSITION, p2 );


	heart = (POS**)calloc( LAYERS, sizeof(POS*) );
	initHeart2();

	printf("***********************************************\n");
	printf("*   HEART SURFACE                             *\n");
	printf("***********************************************\n");
	printf("* (2x^2 + y^2 + z^2 - 1)^3 -0.1x^2z^3 -y^2z^3 *\n");
	printf("***********************************************\n");
	printf("* code by Mateusz Malczak                     *\n");
	printf("* www.malczak.linuxpl.com                     *\n");
	printf("* www.malczak.info                            *\n");
	printf("***********************************************\n");
	glutMainLoop();


         for ( int i=0; i<LAYERS; i++ )
          free( heart[i] );
	free( heart );

   return 0;
}