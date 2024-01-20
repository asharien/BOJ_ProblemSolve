using System;
using System.Linq;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int[] BOX = new int[256];
                        int N = int.Parse(Console.ReadLine());
                        for(int i=0; i<N; i++){
                                BOX[i] = int.Parse(Console.ReadLine());
                        }
                        if(BOX[1]-BOX[0] == BOX[2]-BOX[1]) Console.WriteLine(BOX[N-1]+(BOX[1]-BOX[0]));
                        else Console.WriteLine(BOX[N-1]*(BOX[1]/BOX[0]));
                }
        }
}
