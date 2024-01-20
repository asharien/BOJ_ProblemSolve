using System;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        var line = Console.ReadLine();
                        int ANS =0, HOLDER=0, CNT=0;
                        for(int i=0; i<line.Length; i++){
                                ANS += Convert.ToInt32(line[i])-48;
                        }
                        while(ANS/10 != 0){
                                int TMP = ANS;
                                while(TMP !=0){
                                        HOLDER += TMP%10;
                                        TMP = TMP/10;
                                }
                                ANS = HOLDER;
                                CNT++;
                                HOLDER = 0;
                        }
                        Console.WriteLine((line.Length>1)?CNT+1:CNT);
                        Console.WriteLine((ANS%3==0)?"YES":"NO");
                }
        }
}
