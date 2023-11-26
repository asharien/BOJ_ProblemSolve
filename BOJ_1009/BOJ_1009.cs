using System;

namespace divide_process{
        public class div_process{
                static class PATTERN{
                        public static int[][,] SEQ = new int[10][,] {
                                new int[,]{{10}},
                                new int[,]{{1}},
                                new int[,]{{2,4,8,6}},
                                new int[,]{{3,9,7,1}},
                                new int[,]{{4,6}},
                                new int[,] {{5}},
                                new int[,]{{6}},
                                new int[,]{{7,9,3,1}},
                                new int[,]{{8,4,2,6}},
                                new int[,]{{9,1}}
                        };
                }
                static void Main(string[] args){
                        int CASE = Convert.ToInt32(Console.ReadLine());
                        int A = 0;
                        int B = 0;
                        for(int i=0; i<CASE; i++){
                                var line = Console.ReadLine();
                                var data = line.Split(' ');
                                int TEMP = int.Parse(data[0]);
                                int TEMP2 = int.Parse(data[1]);
                                A = TEMP%10;
                                switch(A){
                                        case 0:
                                                B = 1;
                                                break;
                                        case 1:
                                                B = 1;
                                                break;
                                        case 2:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 3:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 4:
                                                B = TEMP2%2;
                                                if(B == 0){
                                                        B = 2;
                                                }
                                                break;
                                        case 5:
                                                B = 1;
                                                break;
                                        case 6:
                                                B = 1;
                                                break;
                                        case 7:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 8:
                                                B = TEMP2%4;
                                                if(B == 0){
                                                        B = 4;
                                                }
                                                break;
                                        case 9:
                                                B = TEMP2%2;
                                                if(B == 0){
                                                        B = 2;
                                                }
                                                break;
                                        default:
                                                break;
                                }
                                Console.WriteLine(PATTERN.SEQ[A][0, B-1]);


                        }
                }
        }
}
