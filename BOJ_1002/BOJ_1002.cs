using System;
using System.Text;
using System.Linq;
namespace asharien{
    class PROGRAM{
        static void Main(){
            StringBuilder SB = new StringBuilder();
            int N = int.Parse(Console.ReadLine());
            for(int i=0; i<N; i++){
                int[] X = Console.ReadLine().Split().Select(int.Parse).ToArray();
                int X1 = X[0]; int Y1 = X[1]; int R1 = X[2];
                int X2 = X[3]; int Y2 = X[4]; int R2 = X[5];
                double D = Math.Sqrt(Math.Pow((X1-X2),2) + Math.Pow((Y1-Y2),2));
                String ANS = ((X1, Y1, R1) == (X2, Y2, R2))?"-1":((X1, Y1) == (X2, Y2) && R1 != R2)?"0":((R1+R2 == D) || (Math.Abs(R1-R2) == D) && ((X1, Y1) !=(X2, Y2)))? "1":(Math.Abs(R1-R2)<D && D<R1+R2) && ((X1, Y1) !=(X2, Y2))? "2":"0";
                SB.AppendLine(ANS);
            }
            Console.Write(SB);
        }
    }
}
