#include <stdio.h>

int main(){
        int N, i, j, k, l;
        scanf("%d", &N);
        N = N*2-1;
        for(i=0; i<=N/2; i++){
                for(k=i; k<N/2; k++){
                        printf(" ");
                }
                for(k=0; k<=i*2; k++){
                        printf("*");
                }
        printf("\n");
        }
        for(i=N/2-1; i>=0; i--){
                for(k=i; k<N/2; k++){
                        printf(" ");
                }
                for(k=0; k<=i*2; k++){
                        printf("*");
                }
        printf("\n");
        }
        return 0;
}
