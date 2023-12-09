#include <stdio.h>
int main(){
        char L[10];
        int C=0;
        for(int i=0; i<8; i++){
                for(int j=0; j<8; j++){
                        scanf("%c", &L[j]);
                        if(i%2==0 && j%2==0 && L[j] == 'F')C++;
                        else if(i%2 !=0 && j%2 !=0 && L[j] == 'F')C++;
                }
                getchar();
        }
        printf("%d\n", C);
}
