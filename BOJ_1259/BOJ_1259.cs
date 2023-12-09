using System;
namespace asharien{
        public class palindromen{
                static void Main(){
                        int[] ARRAY = new int[100];
                        int[] PALIN = new int[100];
                        int COUNT = 0, Y_FLAG = 0;
                        while(true){
                                int TEMP = int.Parse(Console.ReadLine());
                                if(TEMP == 0){
                                        break;
                                }
                                int LEN = TEMP;
                                while(LEN !=0){
                                        LEN = LEN/10;
                                        COUNT++;
                                }
                                for(int i=0; i<COUNT; i++){
                                        ARRAY[i] = TEMP%10;
                                        PALIN[COUNT-1-i] = TEMP%10;
                                        TEMP = TEMP/10;
                                }
                                for(int i=0; i<COUNT; i++){
                                        if(ARRAY[i]!=PALIN[i]){
                                                Console.WriteLine("no");
                                                Y_FLAG = 0;
                                                break;
                                        }
                                        else{
                                                Y_FLAG = 1;
                                        }
                                }
                                if(Y_FLAG == 1){
                                        Console.WriteLine("yes");
                                }
                                COUNT = 0;
                        }
                }
        }
}
