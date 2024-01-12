#include <stdio.h>
#include <math.h>
int main(){
        float A, B, N, TEMP;
        scanf("%f %f %f", &A, &B, &N);
        TEMP = fmod(A, B);
        for(int i=0; i<N-1; i++){
                TEMP = TEMP*10;
                TEMP = fmod(TEMP, B);
        }
        TEMP = TEMP*10;
        printf("%.0f\n", floor(TEMP/B));
        return 0;
}
