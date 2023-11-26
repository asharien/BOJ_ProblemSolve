using System;
public class divide{
        static void Main(){
                var line = Console.ReadLine();
                var data = line.Split(' ');
                decimal A = decimal.Parse(data[0]);
                decimal B = decimal.Parse(data[1]);
                decimal C = A/B;
                Console.WriteLine(C);
        }
}
