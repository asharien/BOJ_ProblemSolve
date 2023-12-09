#include <iostream>
#include <queue>
#include <string>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        init();
        int N, M, COUNTER_A = 0, COUNTER_B =0, CHECK_FLAG_A = 0, CHECK_FLAG_B = 0;
        string LINE_HOLDER[100];
        int PLACE_HOLDER_A = 0;
        int PLACE_HOLDER_B = 0;
        string BOARD[100];
        char BOARD_CASE_A[100][100] = {{"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}};

        char BOARD_CASE_B[100][100] = {{"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}, {"WBWBWBWB"}, {"BWBWBWBW"}};
        cin >> N >> M;
        for(int i=0; i<N; i++){
                cin >> BOARD[i];
        }
        for(int i=0; i<N-7; i++){
                for(int j=0; j<M-7; j++){
                        for(int k=i; k<i+8; k++){
                                for(int h=j; h<j+8; h++){
                                        if(BOARD[k][h] != BOARD_CASE_A[k-i][h-j]){
                                                COUNTER_A++;
                                        }
                                        else{
                                                continue;
                                        }
                                }
                        }
                        if(PLACE_HOLDER_A == 0 && CHECK_FLAG_A == 0){
                                PLACE_HOLDER_A = COUNTER_A;
                                CHECK_FLAG_A = 1;
                        }
                        if(PLACE_HOLDER_A > COUNTER_A){
                                PLACE_HOLDER_A = COUNTER_A;
                        }
                        COUNTER_A = 0;
                        for(int k=i; k<i+8; k++){
                                for(int h=j; h<j+8; h++){
                                        if(BOARD[k][h] != BOARD_CASE_B[k-i][h-j]){
                                                COUNTER_B++;
                                        }
                                        else{
                                                continue;
                                        }
                                }
                        }
                        if(PLACE_HOLDER_B == 0 && CHECK_FLAG_B == 0){
                                PLACE_HOLDER_B = COUNTER_B;
                                CHECK_FLAG_B = 2;
                        }
                        if(PLACE_HOLDER_B > COUNTER_B){
                                PLACE_HOLDER_B = COUNTER_B;
                        }
                        COUNTER_B = 0;
                }
        }

        if(PLACE_HOLDER_A > PLACE_HOLDER_B){
                cout<<PLACE_HOLDER_B<<'\n';
        }
        else{
                cout<<PLACE_HOLDER_A<<'\n';
        }




        return 0;



}
