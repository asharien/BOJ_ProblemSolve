import java.io.*;

class GLOBAL_TABLE{
        public static int[][] PATTERNS = {{10}, {1}, {2,4,8,6}, {3,9,7,1}, {4,6}, {5}, {6}, {7,9,3,1}, {8,4,2,6}, {9,1}};
}
class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        String[] strNums;
                        String strREADER;
                        int A=0, B=0;
                        int CASE = Integer.parseInt(BR.readLine());
                        for(int i=0; i<CASE; i++){
                                strNums = BR.readLine().split(" ");
                                int TEMP = Integer.parseInt(strNums[0]);
                                int TEMP2 = Integer.parseInt(strNums[1]);
                                A = TEMP%10;
                                switch(A){
                                        case 0:
                                                B = 1;
                                                break;
                                        case 1:
                                                B = 1;
                                                break;
                                        case 2:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 3:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 4:
                                                B = TEMP2%2;
                                                if(B == 0){
                                                        B = 2;
                                                }
                                                break;
                                        case 5:
                                                B = 1;
                                                break;
                                        case 6:
                                                B = 1;
                                                break;
                                        case 7:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 8:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 9:
                                                B = TEMP2%2;
                                                if(B == 0){
                                                        B = 2;
                                                }
                                                break;
                                        default:
                                                break;
                                }
                                BW.write(GLOBAL_TABLE.PATTERNS[A][B-1] + "\n");
                                BW.flush();
                        }

        }
}
