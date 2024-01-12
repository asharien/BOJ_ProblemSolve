import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        StringBuilder SB = new StringBuilder();
                        String[] NUM = BR.readLine().split(" ");
                        String[][] FLOOR = new String[100][100];
                        int N = Integer.parseInt(NUM[0]);
                        int M = Integer.parseInt(NUM[1]);
                        int VWOOD =0;
                        int HWOOD =0;
                        int SEQUENCE = 0;
                        for(int i=0; i<N; i++){
                                FLOOR[i] = BR.readLine().split("");

                        }
                        for(int i=0; i<N; i++){
                                for(int j=0; j<M; j++){
                                        if(FLOOR[i][j].equals("-") == true) SEQUENCE = 1;
                                        else if(FLOOR[i][j].equals("|") == true && SEQUENCE == 1){
                                                HWOOD++;
                                                SEQUENCE = 0;
                                        }
                                        else continue;
                                }
                                HWOOD = HWOOD + SEQUENCE;
                                SEQUENCE = 0;
                        }
                        SEQUENCE = 0;
                        for(int i=0; i<M; i++){
                                for(int j=0; j<N; j++){
                                        if(FLOOR[j][i].equals("|") == true) SEQUENCE = 1;
                                        else if(FLOOR[j][i].equals("-") == true && SEQUENCE == 1){
                                                VWOOD++;
                                                SEQUENCE = 0;
                                        }
                                        else continue;
                                }
                                VWOOD = VWOOD + SEQUENCE;
                                SEQUENCE = 0;
                        }
                        SB.append(VWOOD+HWOOD);
                        BW.write(SB+"\n");
                        BW.flush();

        }
}
