using System;

namespace compare{
        public class comparecondition{
                static void Main(){
                        var line = Console.ReadLine();
                        var data = line.Split(' ');
                        var A = int.Parse(data[0]);
                        var B = int.Parse(data[1]);
                        if(A>B){
                                Console.WriteLine(">");
                        }
                        else if(A<B){
                                Console.WriteLine("<");
                        }
                        else if(A==B){
                                Console.WriteLine("==");
                        }
                        else{
                                Console.WriteLine("ERR");
                        }
                }
        }
}
