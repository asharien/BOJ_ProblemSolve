#include <stdio.h>
#ifndef min
#define min(a, b) (((a)>(b)) ? (b):(a))
#endif
int main(){
        int N;
        scanf("%d", &N);
        int X[1000001] = {0, };
        for(int i=2; i<=N; i++){
                X[i] = X[i-1]+1;
                if(i%2 == 0) X[i] = min(X[i], X[i/2]+1);
                if(i%3 == 0) X[i] = min(X[i], X[i/3]+1);
        }
        printf("%d\n", X[N]);
        return 0;
}
