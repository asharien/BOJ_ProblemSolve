#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
        int N, M, HWOOD=0, VWOOD =0, SEQUENCE=0;
        char FLOOR[64][64];
        char FLAT = '-';
        char VERT = '|';
        scanf("%d %d", &N, &M);
        for(int i=0; i<N; i++){
                scanf("%s", FLOOR[i]);
        }
        for(int i=0; i<N; i++){
                for(int j=0; j<M; j++){
                        if(FLOOR[i][j] == FLAT) SEQUENCE = 1;
                        else if(FLOOR[i][j] == VERT && SEQUENCE == 1){
                                HWOOD++;
                                SEQUENCE = 0;
                        }
                        else continue;
                }
                HWOOD = HWOOD + SEQUENCE;
                SEQUENCE = 0;
        }
        SEQUENCE = 0;
        for(int i=0; i<M; i++){
                for(int j=0; j<N; j++){
                        if(FLOOR[j][i] == VERT) SEQUENCE = 1;
                        else if(FLOOR[j][i] == FLAT && SEQUENCE == 1){
                                VWOOD++;
                                SEQUENCE = 0;
                        }
                        else continue;
                }
                VWOOD = VWOOD + SEQUENCE;
                SEQUENCE = 0;
        }
        printf("%d\n", HWOOD+VWOOD);

        return 0;
}
