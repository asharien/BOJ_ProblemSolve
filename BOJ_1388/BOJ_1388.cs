using System;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        var line = Console.ReadLine();
                        var data = line.Split();
                        int N = int.Parse(data[0]);
                        int M = int.Parse(data[1]);
                        int VWOOD=0, HWOOD=0, SEQUENCE=0;
                        String[] FLOOR = new string[101];
                        for(int i=0; i<N; i++){
                                FLOOR[i] = Console.ReadLine();
                        }
                        for(int i=0; i<N; i++){
                                for(int j=0; j<M; j++){
                                        if(FLOOR[i][j] == '-') SEQUENCE =1;
                                        else if(FLOOR[i][j] == '|' && SEQUENCE ==1){
                                                HWOOD++;
                                                SEQUENCE = 0;
                                        }
                                        else continue;
                                }
                                HWOOD = HWOOD + SEQUENCE;
                                SEQUENCE = 0;
                        }
                        SEQUENCE = 0;
                        for(int i=0; i<M; i++){
                                for(int j=0; j<N; j++){
                                        if(FLOOR[j][i] == '|') SEQUENCE = 1;
                                        else if(FLOOR[j][i] == '-' && SEQUENCE == 1){
                                                VWOOD++;
                                                SEQUENCE = 0;
                                        }
                                        else continue;
                                }
                                VWOOD = VWOOD + SEQUENCE;
                                SEQUENCE = 0;
                        }
                        Console.WriteLine("{0}", HWOOD+VWOOD);
                }
        }
}
