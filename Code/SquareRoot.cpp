#include <iostream>
#include <math.h>
#include <stdio.h>
#include <limits>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <iomanip>

#define sqrt_42 6.48074069840786

using namespace std;
float EPSILON = std::numeric_limits<float>::epsilon();

float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   
	y  = y * ( threehalfs - ( x2 * y * y ) );   
	y  = y * ( threehalfs - ( x2 * y * y ) );
	
	return abs(y);
}

float babylonianSquareRoot(float x, int maxIterations) 
{
    // don't allow negative numbers 
    if (x<0) return 0;
    
    int i =1; 
    
    float y1 = x/2;
    float y2 = (y1 +x/y1)/2;
    
    // now repeat until difference (y1-y2)/y2 -> a very small number
    while( abs(y1/y2-1) > EPSILON )
    {
        // update estimates 
        y1 = y2;
        y2 = (y1 +x/y1)/2;
        ++i;
        if(i >= maxIterations) break;
    }
    return y2;
}    

float halleySquareRoot(float x) 
{
    
    // don't allow negative numbers 
	if (x<0) return 0;
    
    int i =1; // set iteration count to 1
    
    // for first estimate, y1 take
    float y1 = babylonianSquareRoot(x,3);
    y1 = 1/y1;
    
    // for next estimate, y2 take
    float temp = x * y1*y1;
    float y2 = y1*(15-temp*(10 -3*temp))/8;

    // now repeat until temp -> 1
    while( abs(temp-1.0) > EPSILON*10 ) // minimum allowed on my PC
    {
        // update estimates 
        y1 = y2;
        temp = x * y1*y1;
        y2 = y1*(15-temp*(10 -3*temp))/8; 
        ++i;      
    }
    return 1/y2;
}


int main(){ 
    float ans;
	float time_taken;
	
	cout << "Comparison of different methods to compute the square root of 42\n";
	cout << "----------------------------------------------------------------\n\n";
	
	// Lookup method 
	clock_t tStart = clock();
	ans = sqrt_42;
  	time_taken = 1000*(double)(clock() - tStart)/CLOCKS_PER_SEC;
  	
    cout << "Lookup method value " << setw(20) << right << "= " << std::fixed << setprecision(5) << ans;
    cout << setw(20) << right << "\tTime taken " << std::fixed << setprecision(5) << time_taken << " ms\n";

	// Quake III Arena Newton's method https://en.wikipedia.org/wiki/Fast_inverse_square_root
	tStart = clock();
    ans = Q_rsqrt(1.0/42.0);
  	time_taken = 1000*(double)(clock() - tStart)/CLOCKS_PER_SEC;
  	
    cout << "Quake III Arena Newton's method value " << setw(1) << right << "= " << std::fixed << setprecision(5) << ans;
    cout << setw(20) << right << "\tTime taken " << std::fixed << setprecision(5) << time_taken << " ms";
    cout << setw(10) << right << "\tApproximation Error = " << abs(ans-sqrt_42) << "\n";
	
	
	// std::sqrt
	tStart = clock();
    ans = sqrt(42.0);
	time_taken = 1000*(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout << "Standard Square Root method value " << setw(6) << right << "= " << std::fixed << setprecision(5) << ans;
    cout << setw(20) << right << "\tTime taken " << std::fixed << setprecision(5) << time_taken << " ms";
    cout << setw(10) << right << "\tApproximation Error = " << abs(ans-sqrt_42) << "\n";	


	// Babylonian's method https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
	tStart = clock();
	ans = babylonianSquareRoot(42.0,3);		
	time_taken = 1000*(double)(clock() - tStart)/CLOCKS_PER_SEC;
	
	cout << "Babylonian method value " << setw(16) << right << "= " << std::fixed << setprecision(5) << ans;
    cout << setw(20) << right << "\tTime taken " << std::fixed << setprecision(5) << time_taken << " ms";
    cout << setw(10) << right << "\tApproximation Error = " << abs(ans-sqrt_42) << "\n";

	// Halley's method https://en.wikipedia.org/wiki/Halley%27s_method
	tStart = clock();
    ans = halleySquareRoot(42.0);
  	time_taken = 1000*(double)(clock() - tStart)/CLOCKS_PER_SEC;
	cout << "Halley's method value " << setw(18) << right << "= " << std::fixed << setprecision(5) << ans;
    cout << setw(20) << right << "\tTime taken " << std::fixed << setprecision(5) << time_taken << " ms";
    cout << setw(10) << right << "\tApproxiamtion Error = " << abs(ans-sqrt_42) << "\n";

	
	// while(1){
	//   printf("can i haz a job plz\n");
	// }
	
	return 0;
}
