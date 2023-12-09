#include <stdio.h>
#include <string.h>

int main(){
        int N, M, COUNTER_A=0, COUNTER_B=0, CHECK = 0, CHECK2 = 0;
        int PLACE_HOLDER_A = 0;
        int PLACE_HOLDER_B = 0;
        char BOARD[100][100];
        char LINE_HOLDER[100];
        char BOARD_CASE_A[100][100] = {{"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}};
        char BOARD_CASE_B[100][100] = {{"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}};
        scanf("%d %d", &N, &M);
        for(int i=0; i<N; i++){
                scanf("%s", LINE_HOLDER);
                strcpy(BOARD[i], LINE_HOLDER);
        }
        for(int i=0; i<N-7; i++){
                for(int j=0; j<M-7; j++){
                        for(int k=i; k<i+8; k++){
                                for(int l=j; l<j+8; l++){
                                        if(BOARD[k][l] != BOARD_CASE_A[k-i][l-j]){
                                                COUNTER_A++;

                                        }
                                        else{
                                                continue;
                                        }
                                }
                        }
                        if(PLACE_HOLDER_A == 0 && CHECK == 0){
                                PLACE_HOLDER_A = COUNTER_A;
                                CHECK = 1;
                        }
                        if(PLACE_HOLDER_A > COUNTER_A){
                                PLACE_HOLDER_A = COUNTER_A;
                        }
                        COUNTER_A = 0;
                        for(int k=i; k<i+8; k++){
                                for(int l=j; l<j+8; l++){
                                        if(BOARD[k][l] != BOARD_CASE_B[k-i][l-j]){
                                                COUNTER_B++;
                                        }
                                        else{
                                                continue;
                                        }
                                }
                        }
                        if(PLACE_HOLDER_B == 0 && CHECK2 == 0){
                                PLACE_HOLDER_B = COUNTER_B;
                                CHECK2 = 2;
                        }
                        if(PLACE_HOLDER_B > COUNTER_B){
                                PLACE_HOLDER_B = COUNTER_B;
                        }
                        COUNTER_B = 0;
                }
        }
        if(PLACE_HOLDER_A > PLACE_HOLDER_B){
                printf("%d\n", PLACE_HOLDER_B);
        }
        else if(PLACE_HOLDER_B > PLACE_HOLDER_A){
                printf("%d\n", PLACE_HOLDER_A);
        }
        else{
                printf("%d\n", PLACE_HOLDER_A);
        }
        return 0;
}
