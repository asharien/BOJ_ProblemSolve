import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
class Main{
        public static void main(String[] args)
                        throws IOException{
                BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));

                double INPUTS[ ] = new double[2];
                String[] strNums;
                strNums = BR.readLine().split(" ");
                for(int i =0; i<strNums.length; i++){
                        INPUTS[i] = Double.parseDouble(strNums[i]);
                }
                double RESULT;
                RESULT = INPUTS[0]/INPUTS[1];
                System.out.println(RESULT);
        }
}
