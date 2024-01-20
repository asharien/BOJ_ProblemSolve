#include <stdio.h>
int main(){
        int N, F=1, S=1;
        int TROPHY[51];
        scanf("%d", &N);
        for(int i=0; i<N; i++) scanf(" %d", &TROPHY[i]);
        int HISTORY = TROPHY[0];
        for(int i=0; i<N; i++){
                if (TROPHY[i] > HISTORY){
                        F+=1;
                        HISTORY = TROPHY[i];
                }
        }
        HISTORY = TROPHY[N-1];
        for(int i=N-1; i>=0; i--){
                if(TROPHY[i] > HISTORY){
                        S += 1;
                        HISTORY = TROPHY[i];
                }
        }
        printf("%d\n%d\n", F, S);
        return 0;

}
