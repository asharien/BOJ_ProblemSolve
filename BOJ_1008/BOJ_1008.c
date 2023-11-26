#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main(){

        long double A, B, C;
        scanf("%Lf %Lf", &A, &B);
        C = A/ B;
        printf("%.12Lf\n", C);


        return 0;

}
