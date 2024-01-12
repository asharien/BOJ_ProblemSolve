using System;
using System.Linq;
using System.Text;
namespace asharien{
    static class PROGRAM{
        public static void Main(){
            StringBuilder SB = new StringBuilder();
            while(true){
                var N = Console.ReadLine();
                if(N == "0") break;
                int ANS = 0;
                foreach(char i in N){
                    if(i == '1') ANS +=2;
                    else if(i == '0') ANS += 4;
                    else ANS +=3;
                }
                SB.AppendLine((ANS+N.Length+1).ToString("G"));
            }
            Console.Write(SB);
        }
    }
}
