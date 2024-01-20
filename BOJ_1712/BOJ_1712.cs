using System;
using System.Linq;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int[] X = Console.ReadLine().Split().Select(int.Parse).ToArray();
                        double ANS = (X[1]>=X[2])? -1:X[0]/(X[2]-X[1])+1;
                        Console.WriteLine(ANS);
                }
        }
}
