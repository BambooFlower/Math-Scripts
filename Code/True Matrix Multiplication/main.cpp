#include <iostream>

using namespace std;

#define N 2

void multiply(int mat1[][N],
			  int mat2[][N],
			  int res[][N]){
	int i,j,k;
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			res[i][j] = 0;
			for(k=0;k<N;k++)
				res[i][j] += mat1[i][k] * mat2[k][j];
		}
	}			  
}

bool are_equal(int mat1[][N], int mat2[][N]){
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(mat1[i][j] != mat2[i][j])
				return false;
		}
	}
	return true;
}

int main()
{
	int i,j;
	int res[N][N];
	
	int c1_1,c1_2,c2_1,c2_2,c3_1,c3_2,c4_1,c4_2;
	
	int counter = 0;
		
	for(c1_1=1;c1_1<10;c1_1++){
	for(c1_2=0;c1_2<10;c1_2++){
		for(c2_1=1;c2_1<10;c2_1++){
		for(c2_2=0;c2_2<10;c2_2++){
			for(c3_1=1;c3_1<10;c3_1++){
			for(c3_2=0;c3_2<10;c3_2++){
				for(c4_1=1;c4_1<10;c4_1++){
				for(c4_2=0;c4_2<10;c4_2++){
					
					int mat0[N][N] = { {c1_1*10 + c1_2, c2_1*10 + c2_2},
    			     	     {c3_1*10 + c3_2, c4_1*10 + c4_2}
     			                	  };
     			    
					int mat1[N][N] = { {c1_1,c2_1},
					   	     {c3_1,c4_1}
					 		};
					int mat2[N][N] = { {c1_2,c2_2},
					   		 {c3_2,c4_2}
					 		};
					 		
				 	multiply(mat1,mat2,res);
					if(are_equal(res,mat0)){
						for(i=0; i<N; i++){
							for(j=0;j<N;j++)
								cout << mat0[i][j] << " ";
//							cout << "\n";
						}
						cout << "\n";
						counter++;
					}
					
				}
				}
			}
			}
			
		}
		}
	}
	}
	cout << counter << endl;
	return 0;
}
