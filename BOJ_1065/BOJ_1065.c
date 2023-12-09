#include <stdio.h>
#include <math.h>
int main(){
        int N, ANS=99;
        scanf("%d", &N);
        if(N<100) printf("%d\n", N);
        else{
                for(int i=100; i<N+1; i++) if(i%10-floor(i%100/10) == floor(i%100/10)-i/100) ANS++;
                printf("%d\n", ANS);
        }
        return 0;
}
