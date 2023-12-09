using System;
namespace escape_from_rectangle{
        class Program{
                static void Main(string[] args){
                        var line = Console.ReadLine();
                        var data = line.Split(' ');
                        int X = int.Parse(data[0]);
                        int Y = int.Parse(data[1]);
                        int W = int.Parse(data[2]);
                        int H = int.Parse(data[3]);
                        int TO_BORDER_X = W-X;
                        int TO_BORDER_Y = H-Y;
                        int PLACE_HOLDER = Math.Min(X,Y);
                        PLACE_HOLDER = Math.Min(PLACE_HOLDER, TO_BORDER_X);
                        PLACE_HOLDER = Math.Min(PLACE_HOLDER, TO_BORDER_Y);
                        Console.WriteLine(PLACE_HOLDER);

                }
        }
}
