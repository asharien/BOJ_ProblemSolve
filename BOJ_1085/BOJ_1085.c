#include <stdio.h>

int main(){
        int X, Y, W, H, PLACE_HOLDER, TO_BORDER_X, TO_BORDER_Y;
        scanf("%d %d %d %d", &X, &Y, &W, &H);
        TO_BORDER_X = W-X;
        TO_BORDER_Y = H-Y;
        if(X>Y){
                PLACE_HOLDER = Y;
        }
        else if(X < Y){
                PLACE_HOLDER = X;
        }
        else if(X == Y){
                PLACE_HOLDER = X;
        }

        if(PLACE_HOLDER > TO_BORDER_X){
                PLACE_HOLDER = TO_BORDER_X;
        }
        if(PLACE_HOLDER > TO_BORDER_Y){
                PLACE_HOLDER = TO_BORDER_Y;
        }
        printf("%d", PLACE_HOLDER);

        return 0;
}
