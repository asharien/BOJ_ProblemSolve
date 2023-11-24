import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
class Main{
        public static void main(String[] args)
                        throws IOException{
                BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                int INPUTS[ ] = new int[2];
                String[] strNums;
                strNums = BR.readLine().split(" ");
                for(int i =0; i<strNums.length; i++){
                        INPUTS[i] = Integer.parseInt(strNums[i]);
                }
                int RESULT;
                RESULT = INPUTS[0]-INPUTS[1];
                System.out.println(RESULT);
        }
}
