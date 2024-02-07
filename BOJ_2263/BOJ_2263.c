#include <stdio.h>
int POS[100001], IN[100001], LOOK[100001];
void PRE(int INS, int INE, int POSS, int POSE){
        if((INS>INE)&&(POSS>POSE)) return;
        int ROOT = POS[POSE];
        int LEFT = LOOK[ROOT] - INS;
        int RIGHT = INE - LOOK[ROOT];
        printf("%d ", ROOT);
        PRE(INS, INS+LEFT-1, POSS, POSS+LEFT-1);
        PRE(INE-RIGHT+1, INE, POSE-RIGHT, POSE-1);
}
int main(){
        int N;
        scanf("%d", &N);
        for(int i=0; i<N; i++){
                scanf(" %d", &IN[i]);
                LOOK[IN[i]]=i;
        }
        for(int i=0; i<N; i++){
                scanf(" %d", &POS[i]);
        }
        PRE(0, N-1, 0, N-1);
        printf("\n");

}
