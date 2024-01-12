using System;
using System.Linq;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int[] DB = Console.ReadLine().Split().Select(int.Parse).ToArray();
                        int[] NEWMAP = new int[1024];
                        int A = DB[0]; int B = DB[1];
                        int REPEAT = 0, CNT = 0;
                        while(true){
                                if(CNT == B+1) break;
                                REPEAT += 1;
                                for(int i=0; i<REPEAT; i++){
                                        if(CNT == B+1) break;
                                        NEWMAP[CNT+1] = NEWMAP[CNT]+REPEAT;
                                        CNT += 1;
                                }
                        }
                        Console.WriteLine(NEWMAP[B]-NEWMAP[A-1]);

                }
        }
}
