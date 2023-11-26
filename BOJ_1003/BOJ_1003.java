import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
class GLOBALS{
        public static int[] COLLECTION = new int [50];

}
class Main{
        public static void main(String[] args) throws IOException{
                BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                int CASE, N;
                CASE = Integer.parseInt(BR.readLine());
                FIBONACCI(0);
                FIBONACCI(1);
                FIBONACCI(2);
                for(int i  = 0; i<CASE; i++){
                        N = Integer.parseInt(BR.readLine());
                        if(N == 0){
                                System.out.println("1 0");
                        }
                        else if(N == 1){
                                System.out.println("0 1");
                        }
                        else if(N == 2){
                                System.out.println("1 1");
                        }
                        else{
                                FIBONACCI(N);
                                System.out.println(GLOBALS.COLLECTION[N-1]+ " " + GLOBALS.COLLECTION[N]);
                        }
                }
        }
        public static int FIBONACCI(int RECALL){
                if(RECALL <= 0){
                        GLOBALS.COLLECTION[0] = 0;
                        return 0;
                }
                else if(RECALL == 1){
                        GLOBALS.COLLECTION[1] = 1;
                        return 1;
                }
                if(GLOBALS.COLLECTION[RECALL] != 0){
                        return GLOBALS.COLLECTION[RECALL];
                }
                else{
                        GLOBALS.COLLECTION[RECALL] = FIBONACCI(RECALL-1) + FIBONACCI(RECALL-2);
                        return GLOBALS.COLLECTION[RECALL];
                }
        }
}
