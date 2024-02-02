using System;
using System.Linq;
using System.Numerics;
namespace ashrein{
	class PROGRAM{
		static void Main(){
			int N = int.Parse(Console.ReadLine());
			long[] L = Console.ReadLine().Split().Select(long.Parse).ToArray();
			Array.Sort(L);
			long A = 0;
			for(int i=0; i<N; i++){
				long TARGET = L[i];
				long[] TMP = L.Where((source, index) => index !=i).ToArray();
				int UP =0, DW=TMP.Length-1;
				while(UP<DW){
					long S = TMP[UP] + TMP[DW];
					if(S<TARGET) UP +=1;
					else if(S>TARGET) DW -=1;
					else{
						A += 1;
						UP +=1;
						DW -= 1;
						break;
					}
				}
			}
			Console.WriteLine(A);
		}
	}
}
