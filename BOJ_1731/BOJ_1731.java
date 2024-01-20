import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int N = Integer.parseInt(BR.readLine());
                        int[] DB = new int[256];
                        for(int i=0; i<N; i++){
                                DB[i] = Integer.parseInt(BR.readLine());
                        }
                        int GAP = DB[1]-DB[0];
                        int MUL = DB[1]/DB[0];
                        int ANS = (DB[2]-DB[1] == DB[1]-DB[0])? DB[N-1]+GAP : DB[N-1]*MUL;
                        BW.write(ANS+"\n");
                        BW.flush();

        }
}
