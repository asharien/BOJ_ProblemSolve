using System;
using System.Linq;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int[] X = new int[128];
                        int[] L = Console.ReadLine().Split().Select(int.Parse).ToArray();
                        for(int i=1; i<=L[0]; i++){
                                for(int j=1; j<=L[1]; j++){
                                        for(int k=1; k<=L[2]; k++){
                                                X[i+j+k] += 1;
                                        }
                                }
                        }
                        int ANS = X.Max();
                        int COLL = Array.IndexOf(X, ANS);
                        Console.WriteLine(COLL);

                }
        }
}
