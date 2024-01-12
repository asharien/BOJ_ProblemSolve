using System;
using System.Linq;
using System.Text;
using System.Numerics;
namespace asharien{
    static class PROGRAM{
        public static void Main(){
            StringBuilder SB = new StringBuilder();
            int CASE = int.Parse(Console.ReadLine());
            for(int i=0; i<CASE; i++){
                BigInteger[] N = Console.ReadLine().Split().Select(BigInteger.Parse).ToArray();
                if(BigInteger.Compare(N[0], N[1])>=-1){
                    SB.AppendLine("yes");
                }
                else{
                    SB.AppendLine("no");
                }
            }
            Console.Write(SB);
        }
    }
}
