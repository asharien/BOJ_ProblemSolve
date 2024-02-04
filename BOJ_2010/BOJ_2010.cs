using System;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        long N = long.Parse(Console.ReadLine());
                        long ANS =0;
                        for(long i=0; i<N; i++){
                                long TEMP = long.Parse(Console.ReadLine());
                                ANS += TEMP;
                        }
                        Console.WriteLine(ANS-N+1);
                }
        }
}
