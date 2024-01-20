#include <stdio.h>
int main(){
        int N;
        int DATABASE[101] = {0, };
        scanf("%d", &N);
        for(int i=0; i<N; i++){
                scanf("%d", &DATABASE[i]);
        }
        if(DATABASE[1]-DATABASE[0] == DATABASE[2]-DATABASE[1]) printf("%d\n", DATABASE[N-1]+(DATABASE[1]-DATABASE[0]));
        else if(DATABASE[1]/DATABASE[0] == DATABASE[2]/DATABASE[1]) printf("%d\n", DATABASE[N-1]*(DATABASE[1]/DATABASE[0]));
        return 0;
}
