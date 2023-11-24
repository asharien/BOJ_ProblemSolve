using System;
namespace plus{
        class Program{
                static void Main(){
                        var line = Console.ReadLine();
                        var data = line.Split(' ');
                        int A = int.Parse(data[0]);
                        int B = int.Parse(data[1]);
                        int C = A+B;
                        Console.WriteLine(C);
                }
        }
}
