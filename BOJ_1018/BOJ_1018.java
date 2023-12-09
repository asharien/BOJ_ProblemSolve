import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
class G_VAL{
        public static String[] BOARD = new String[200];
        public static String[] BOARD_CASE_A = {"BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"};
        public static String[] BOARD_CASE_B = {"WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"};
}
class Main{
        public static void main(String[] args)
                throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        String[] strNums;
                        String strREADER;
                        strNums = BR.readLine().split(" ");
                        int N = Integer.parseInt(strNums[0]);
                        int M = Integer.parseInt(strNums[1]);
                        int COUNT_A =0, COUNT_B = 0, PLACE_HOLDER_A = 0, PLACE_HOLDER_B = 0, FLAG_A = 0, FLAG_B = 0;
                        int PLACE_HOLDER;
                        for(int i=0; i<N; i++){
                                strREADER = BR.readLine();
                                G_VAL.BOARD[i] = strREADER;
                        }
                        for(int i=0; i<N-7; i++){
                                for(int j=0; j<M-7; j++){
                                        for(int k=i; k<i+8; k++){
                                                for(int h=j; h<j+8; h++){
                                                        if(G_VAL.BOARD[k].charAt(h) != G_VAL.BOARD_CASE_A[k-i].charAt(h-j))
                                                                COUNT_A++;

                                                }
                                        }
                                        if(PLACE_HOLDER_A == 0 && FLAG_A == 0){
                                                PLACE_HOLDER_A = COUNT_A;
                                                FLAG_A = 1;
                                        }
                                        if(PLACE_HOLDER_A > COUNT_A)
                                                PLACE_HOLDER_A = COUNT_A;
                                        COUNT_A = 0;
                                        for(int k=i; k<i+8; k++){
                                                for(int h=j; h<j+8; h++){
                                                        if(G_VAL.BOARD[k].charAt(h) != G_VAL.BOARD_CASE_B[k-i].charAt(h-j))
                                                                COUNT_B++;

                                                }
                                        }
                                        if(PLACE_HOLDER_B == 0 && FLAG_B == 0){
                                                PLACE_HOLDER_B = COUNT_B;
                                                FLAG_B = 1;
                                        }
                                        if(PLACE_HOLDER_B>COUNT_B)
                                                PLACE_HOLDER_B = COUNT_B;
                                        COUNT_B = 0;
                                }
                        }
                        PLACE_HOLDER = Math.min(PLACE_HOLDER_A, PLACE_HOLDER_B);
                        BW.write(PLACE_HOLDER + "\n");
                        BW.flush();
                }
}
