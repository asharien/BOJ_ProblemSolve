using System;

public class CHESS_BOARD{                                                                                                           static void Main(){
                var line = Console.ReadLine();
                var data = line.Split(' ');                                                                                                 int N = int.Parse(data[0]);
                int M = int.Parse(data[1]);
                int COUNTER_A = 0, COUNTER_B = 0, PLACE_HOLDER_A = 0, PLACE_HOLDER_B = 0, CHECK_FLAG_A = 0, CHECK_FLAG_B =0;
                string[,] BOARD_CASE_A = {{"BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"}};
                string[,] BOARD_CASE_B = {{"WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"}};
                string[] BOARD = new string[1000];
                for(int i=0; i<N; i++){
                        line = Console.ReadLine();
                        BOARD[i] = line;
                }
                for(int i=0; i<N-7; i++){
                        for(int j=0; j<M-7; j++){
                                for(int k=i; k<i+8; k++){
                                        for(int h=j; h<j+8; h++){
                                                if(BOARD[k][h] != BOARD_CASE_A[0, k-i][h-j]){
                                                        COUNTER_A++;
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
                                                if(BOARD[k][h] != BOARD_CASE_B[0, k-i][h-j]){
                                                        COUNTER_B++;
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
                        Console.WriteLine(PLACE_HOLDER_B);
                }
                else if(PLACE_HOLDER_B > PLACE_HOLDER_A){
                        Console.WriteLine(PLACE_HOLDER_A);
                }
                else{
                        Console.WriteLine(PLACE_HOLDER_B);
                }
        }
}
