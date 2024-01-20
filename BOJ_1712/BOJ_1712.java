import java.io.*;
import java.util.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        StringTokenizer ST = new StringTokenizer(BR.readLine());
                        int A = Integer.parseInt(ST.nextToken());
                        int B = Integer.parseInt(ST.nextToken());
                        int C = Integer.parseInt(ST.nextToken());
                        String ANS = (B>=C)? "-1":String.valueOf(A/(C-B)+1);
                        BW.write(ANS +"\n");
                        BW.flush();

        }
}
