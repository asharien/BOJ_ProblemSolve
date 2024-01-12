import java.io.*;
class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        String[] DATA = BR.readLine().split(" ");
                        int[] TRACK = new int[1024];
                        int A = Integer.parseInt(DATA[0]);
                        int B = Integer.parseInt(DATA[1]);
                        int NUM=0, CNT =0;
                        while(true){
                                if(CNT == B+1) break;
                                NUM++;
                                for(int i=0; i<NUM; i++){
                                        if(CNT == B+1) break;
                                        TRACK[CNT+1] = TRACK[CNT]+NUM;
                                        CNT++;
                                }
                        }
                        BW.write(TRACK[B]-TRACK[A-1]+"\n");
                        BW.flush();
        }
}
