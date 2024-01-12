#include <stdio.h>
int main(){
        int A, B, CNT =0, i=0;
        int CSUM[1024] = {0, };
        scanf("%d %d", &A, &B);
        while(1){
                i++;
                for(int j=0; j<i; j++){
                        if(CNT == B+1) break;
                        CSUM[CNT+1] = CSUM[CNT]+i;
                        CNT++;
                }
                if(CNT == B+1) break;
        }
        printf("%d\n", CSUM[B]-CSUM[A-1]);
        return 0;
}
