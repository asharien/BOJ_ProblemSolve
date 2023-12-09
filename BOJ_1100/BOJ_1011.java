import java.io.*;
import java.util.*;
class Main{
        public static void main(String[] args)
                        throws IOException{
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int C =0;
                        for(int i=0; i<8; i++){
                                String L = BR.readLine();
                                if(i%2 == 0){
                                        for(int j=0; j<8; j++) if(L.charAt(j) == 'F' && j%2==0) C++;
                                }
                                else{
                                        for(int j=0; j<8; j++) if(L.charAt(j) == 'F' && j%2!=0) C++;
                                }
                        }
                        BW.write(C +"\n");
                        BW.flush();

        }
}
