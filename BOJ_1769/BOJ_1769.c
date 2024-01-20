#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
        char X[1000001];
        scanf("%s", X);
        long L = strlen(X);
        int CNT=0, FAKE=0;
        long ANS =0, TMP=0, TMP2=0;
        for(int i=0; i<L; i++){
                FAKE = (int)X[i]-48;
                ANS += FAKE;
        }
        while(ANS/10 != 0){
                TMP = ANS;
                while(TMP !=0){
                        TMP2 += TMP%10;
                        TMP = TMP/10;
                }
                ANS = TMP2;
                CNT++;
                TMP2 =0;
        }
        printf("%d\n", (L>1)?CNT+1:CNT);
        printf("%s\n", (ANS%3==0)?"YES":"NO");
}
