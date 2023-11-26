using System;
using System.Text;
namespace asharien{
    class PROGRAM{
        static void Main(){
            StringBuilder SB = new StringBuilder();
            int N = int.Parse(Console.ReadLine());
            for(int i=0; i<N; i++){
                long[] DATA = Console.ReadLine().Split().Select(long.Parse).ToArray();
                SB.AppendLine(Convert.ToString(Math.Truncate(Math.Sqrt((4*(DATA[1]-DATA[0]))-1))));
            }
            Console.Write(SB);
        }
    }
}
