#include <stdio.h>
int main(){
        int A, B, C;
        scanf("%d %d %d", &A, &B, &C);
        double X = A/(C-B);
        printf("%.0f\n", (B>=C)? -1:X+1);
        return 0;
}
