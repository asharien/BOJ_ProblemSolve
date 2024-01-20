import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        StringBuilder SB = new StringBuilder();
                        String X = BR.readLine();
                        int ANS=0, CNT=0, HOLD=0;
                        for(int i=0; i<X.length(); i++){
                                ANS += Integer.valueOf(X.charAt(i))-48;
                        }
                        while(ANS/10 !=0){
                                int TMP = ANS;
                                while(TMP !=0){
                                        HOLD += TMP%10;
                                        TMP = TMP/10;
                                }
                                ANS = HOLD;
                                CNT++;
                                HOLD = 0;
                        }
                        SB.append((X.length()>1)?CNT+1:CNT).append("\n").append((ANS%3 == 0)?"YES":"NO");
                        BW.write(SB+"\n");
                        BW.flush();

        }
}
