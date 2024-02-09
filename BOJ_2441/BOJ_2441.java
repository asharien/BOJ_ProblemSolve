import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        StringBuilder SB = new StringBuilder();
                        int N = Integer.parseInt(BR.readLine());
                        for(int i=0; i<N; i++){
                                for(int j=0; j<i; j++){
                                        SB.append(" ");
                                }
                                for(int k=0; k<N-i; k++){
                                        SB.append("*");
                                }
                                SB.append("\n");
                        }
                        BW.write(SB + "");
                        BW.flush();

        }
}
