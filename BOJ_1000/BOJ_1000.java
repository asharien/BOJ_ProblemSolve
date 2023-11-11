import java.io.BufferedReader;
import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.IOException;
class Main{
        public static void main(String[] args)
        throws IOException{
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        int NUM[] = new int[2];
        String[] strNums;
        strNums = bi.readLine().split(" ");
        for(int i =0; i<strNums.length; i++){
                NUM[i] = Integer.parseInt(strNums[i]);
        }
        int RESULT;
        RESULT = NUM[0]+NUM[1];
        System.out.println(RESULT);


        }
}
