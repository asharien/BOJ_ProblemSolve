using System;
using System.Linq;
using System.Text;
using System.Numerics;
namespace asharien{
    static class PROGRAM{
        public static void Main(){
            int testCases = int.Parse(Console.ReadLine());
            for (int t = 0; t < testCases; t++){
                string[] input = Console.ReadLine().Split();
                int N = int.Parse(input[0]);
                int M = int.Parse(input[1]);
                BigInteger result = CalculateFactorial(M)/(CalculateFactorial(M-N)*CalculateFactorial(N));
                Console.WriteLine(result);
        }
        }
        static BigInteger CalculateFactorial(int num){
            if (num == 0 || num == 1) return 1;
            else{
                BigInteger result = 1;
                for (int i = 2; i <= num; i++) result *= i;
                return result;
            }
        }
    }
}
