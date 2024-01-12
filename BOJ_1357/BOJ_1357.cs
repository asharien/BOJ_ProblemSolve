using System;
using System.Linq;
using System.Text;
namespace asharien{
    static class PROGRAM{
        static void Main(){
            int[] XY = Console.ReadLine().Split().Select(int.Parse).ToArray();
            String X = XY[0].ToString();
            String Y = XY[1].ToString();
            Console.WriteLine(FLIP((FLIP(X)+FLIP(Y)).ToString()));

        }
        public static int FLIP(this string S){
            char[] X = S.ToCharArray();
            Array.Reverse(X);
            int ANS = Convert.ToInt32(new string(X)); 
            return ANS;
        }
    }
}
