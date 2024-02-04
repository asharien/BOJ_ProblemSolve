import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        long N = Long.parseLong(BR.readLine());
                        long ANS = 0;
                        for(long i=0; i<N; i++){
                                long TEMP = Long.parseLong(BR.readLine());
                                ANS += TEMP;
                        }
                        BW.write(ANS-N+1 + "\n");
                        BW.flush();

        }
}
