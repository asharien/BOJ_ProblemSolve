using System;
using System.Linq;
namespace asharien{
        class PROGRAM{
                static void Main(){
                        int C=0;
                        for(int i=0; i<8; i++){
                                var line = Console.ReadLine();
                                if(i%2==0){
                                        for(int j=0; j<8; j++){
                                                if(j%2==0 && line[j]=='F') C++;
                                        }
                                }
                                else{
                                        for(int j=0; j<8; j++){
                                                if(j%2 != 0 && line[j]=='F') C++;
                                        }
                                }
                        }
                        Console.WriteLine(C);
                }
        }
}
