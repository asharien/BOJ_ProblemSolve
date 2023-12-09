#include <stdio.h>
int main(){
        int A, B, C, PLACEHOLDER = 0, ANS;
        int PATHFINDER[82] = {0, };
        scanf("%d %d %d", &A, &B, &C);
        for(int i=1; i<=A; i++){
                for(int j=1; j<=B; j++){
                        for(int k=1; k<=C; k++){
                                PATHFINDER[i+j+k] += 1;
                        }
                }
        }
        for(int i=0; i<82; i++){
                if(PATHFINDER[i]>PLACEHOLDER){
                        PLACEHOLDER = PATHFINDER[i];
                        ANS = i;
                }
        }
        printf("%d\n", ANS);
        return 0;
}
