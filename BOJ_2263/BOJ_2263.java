import java.io.*;

class Main{
        static StringBuilder SB = new StringBuilder();
        static int[] IN;
        static int[] POST;
        static int[] TREE = new int[100001];
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int N = Integer.parseInt(BR.readLine());
                        IN = new int[N];
                        POST = new int[N];
                        String[] F = BR.readLine().split(" ");
                        String[] S = BR.readLine().split(" ");
                        for(int i=0; i<N; i++){
                                IN[i] = Integer.parseInt(F[i]);
                                POST[i] = Integer.parseInt(S[i]);
                                TREE[IN[i]] = i;
                        }
                        PRE(0, N-1, 0, N-1);
                        BW.write(SB+"\n");
                        BW.flush();
        }
        public static void PRE(int INS, int INE, int POST_S, int POST_E){
                if(INS>INE && POST_S>POST_E) return;
                int ROOT = POST[POST_E];
                int LEFT = TREE[ROOT] - INS;
                int RIGHT = INE - TREE[ROOT];
                SB.append(ROOT).append(" ");
                PRE(INS, INS+LEFT-1, POST_S, POST_S+LEFT-1);
                PRE(INE-RIGHT+1, INE, POST_E-RIGHT, POST_E-1);
        }
}
