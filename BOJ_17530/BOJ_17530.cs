using System;
using System.Linq;
using System.Numerics;
namespace asharien{
	class PROGRAM{
		static void Main(){
			int[] VOTE = new int[1000001];
			int CASE = int.Parse(Console.ReadLine());
			for(int i=0; i<CASE; i++) VOTE[i] = int.Parse(Console.ReadLine());
			Console.WriteLine((VOTE[0]>=VOTE.Max())?"S":"N");
		}
	}
}
