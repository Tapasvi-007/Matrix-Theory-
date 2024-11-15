#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include "A1/matfun.h"
#include "A1/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, int num_points) {
    for (int i = 0; i <= num_points; i++) {
		double temp = (double)i/(double)num_points;
		double temp1 = 1-temp;
        double **output = Matadd(Matscale(A,2,1,temp1),Matscale(B,2,1,temp),2,1);
		printf("%lf,%lf\n",output[0][0],output[1][0]);
		fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output,2);
	}}


int main() {
    double x1, y1, x2, y2, x3, y3,x4,y4;
//    scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &x3, &y3);
    x1 = 4; y1 = 4;
    x2 = -2; y2 = 6;
    x3 = 1; y3 = 5;

    int m = 2, n = 1;
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);
    A[0][0] = x1;
    A[1][0] = y1;
    B[0][0] = x2;
    B[1][0] = y2;
    M[0][0] = x3;
    M[1][0] = y3;

    FILE *fptr;
    fptr = fopen("points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

        point_gen(fptr,A,M,20);


    fclose(fptr);
    return 0;
}
