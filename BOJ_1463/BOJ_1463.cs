using System;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int N = int.Parse(Console.ReadLine());
                        int[] X= new int[N+1];
                        for(int i=2; i<=N; i++){
                                X[i] = X[i-1]+1;
                                if(i%2 ==0) X[i] = Math.Min(X[i], X[i/2]+1);
                                if(i%3 ==0) X[i] = Math.Min(X[i], X[i/3]+1);
                        }
                        Console.WriteLine(X[N]);
                }
        }
}
