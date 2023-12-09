import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main{
        public static void main(String[] args)
        throws IOException{
        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
        String[] strNums;
        strNums = BR.readLine().split(" ");
        int X = Integer.parseInt(strNums[0]);
        int Y = Integer.parseInt(strNums[1]);
        int W = Integer.parseInt(strNums[2]);
        int H = Integer.parseInt(strNums[3]);
        int GAP_X = W-X;
        int GAP_Y = H-Y;
        int PLACE_HOLDER = Math.min(Math.min(X, Y), Math.min(GAP_X, GAP_Y));
        System.out.println(PLACE_HOLDER);
        }
}
