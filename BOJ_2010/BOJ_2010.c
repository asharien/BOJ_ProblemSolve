#include <stdio.h>
int main(){
        long long S=0, T, N;
        scanf("%lld", &N);
        for(long long i=0; i<N; i++){
                scanf("%lld", &T);
                S = S+T;
        }
        printf("%lld\n", S-N+1);
        return 0;
}
