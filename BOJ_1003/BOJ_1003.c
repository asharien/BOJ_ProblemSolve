#include <stdio.h>
int MEMORY[45] ={0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int FIBO(int RECALL){
        if(RECALL <= 0){
                MEMORY[0] = 0;
                return 0;
        }
        else if(RECALL == 1){
                MEMORY[1] = 1;
                return 1;
        }
        if(MEMORY[RECALL] != 0){
                return MEMORY[RECALL];
        }
        else{
                MEMORY[RECALL] = FIBO(RECALL-1)+FIBO(RECALL-2);
                return MEMORY[RECALL];
        }
}

int main(){
        int N, CASE, i, j, k;
        scanf("%d", &CASE);
        for(i=0; i<CASE; i++){
                scanf("%d", &N);
                if(N == 0){
                        printf("1 0\n");
                }
                else if(N == 1){
                        printf("0 1\n");
                }
                else if(N == 2){
                        printf("1 1\n");
                }
                else{
                        FIBO(N);
                        printf("%d %d\n", MEMORY[N-1], MEMORY[N]);
                }
        }
}
