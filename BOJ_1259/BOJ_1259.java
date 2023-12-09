import java.io.*;

class Main{
        public static void main(String[] args)
                        throws IOException{                                                                                                           
                        BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
                        BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
                        int[] ARRAY = new int[100];
                        int[] PALIN = new int[100];
                        int COUNT = 0, Y_FLAG = 0;
                        while(true){
                                int TEMP = Integer.parseInt(BR.readLine());
                                int LEN = TEMP;
                                if(TEMP == 0){
                                        break;
                                }
                                while(LEN != 0){
                                        LEN = LEN/10;
                                        COUNT ++;
                                }
                                for(int i=0; i<COUNT; i++){
                                        ARRAY[i] = TEMP%10;
                                        PALIN[COUNT-1-i] = TEMP%10;
                                        TEMP = TEMP/10;
                                }
                                for(int i=0; i<COUNT; i++){
                                        if(ARRAY[i] != PALIN[i]){
                                                BW.write("no" + "\n");
                                                BW.flush();
                                                Y_FLAG = 0;
                                                break;
                                        }
                                        else{
                                                Y_FLAG = 1;
                                        }
                                }
                                if(Y_FLAG == 1){
                                        BW.write("yes" + "\n");
                                        BW.flush();
                                }
                                COUNT = 0;

                        }                                                                                                     
        }
}
