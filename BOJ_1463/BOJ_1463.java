import java.io.*;
import java.util.*;
class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int N = Integer.parseInt(BR.readLine());
                        int[] X = new int[N+1];
                        for(int i=2; i<=N; i++){
                                X[i] = X[i-1]+1;
                                if(i%2 == 0) X[i] = Math.min(X[i], X[i/2]+1);
                                if(i%3 == 0) X[i] = Math.min(X[i], X[i/3]+1);
                        }
                        BW.write(X[N] + "\n");
                        BW.flush();

        }
}
