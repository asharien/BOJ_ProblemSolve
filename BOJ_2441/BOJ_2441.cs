using System;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int N = int.Parse(Console.ReadLine());
                        for(int i=0; i<N; i++){
                                for(int j=0; j<i; j++){
                                        Console.Write(" ");
                                }
                                for(int k=0; k<N-i; k++){
                                        Console.Write("*");
                                }
                                Console.WriteLine();
                        }
                }
        }
}
