using System;

namespace FIBONACCI{
        public class FIBONACCI{
                static void Main(){
                        int CASE = Convert.ToInt32(Console.ReadLine());
                        for(int i=0; i<CASE; i++){
                                int N = Convert.ToInt32(Console.ReadLine());
                                if(N == 0){
                                        Console.WriteLine("1 0");
                                }
                                else if(N == 1){
                                        Console.WriteLine("0 1");
                                }
                                else if(N == 2){
                                        Console.WriteLine("1 1");
                                }
                                else{
                                        FIBOS(N);
                                        Console.WriteLine("{0} {1}", TABLE[N-1], TABLE[N]);
                                }
                        }


                }
                public static int[] TABLE = new int[41];
                static int FIBOS(int RECALL){
                        if(RECALL <= 0){
                                TABLE[0] = 0;
                                return 0;
                        }
                        else if(RECALL == 1){
                                TABLE[1] = 1;
                                return 1;
                        }
                        if(TABLE[RECALL] != 0){
                                return TABLE[RECALL];
                        }
                        else{
                                TABLE[RECALL] = FIBOS(RECALL-1) + FIBOS(RECALL-2);
                                return TABLE[RECALL];
                        }
                }
        }
}
