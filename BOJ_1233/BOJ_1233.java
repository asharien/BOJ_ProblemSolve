import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int X[] = new int[101];
                        StringTokenizer ST = new StringTokenizer(BR.readLine());
                        int A = Integer.parseInt(ST.nextToken());
                        int B = Integer.parseInt(ST.nextToken());
                        int C = Integer.parseInt(ST.nextToken());
                        for(int i=1; i<=A; i++){
                                for(int j=1; j<=B; j++){
                                        for(int k=1; k<=C; k++){
                                                X[i+j+k] += 1;
                                        }
                                }
                        }
                        List <Integer> TMP = Arrays.stream(X).boxed().collect(Collectors.toList());
                        int ANS = TMP.indexOf(Collections.max(TMP));
                        BW.write(ANS + "\n");
                        BW.flush();
        }
}
