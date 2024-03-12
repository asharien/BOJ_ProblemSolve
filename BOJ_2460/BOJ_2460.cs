using System;
using System.Linq;
using System.Text;
namespace asharien{
	class PROGRAM{
		static void Main(){
			int ANS = 0, HOLDER = 0;
			for(int i=0; i<10; i++){
				int[] X = Console.ReadLine().Split().Select(int.Parse).ToArray();
				ANS -= X[0];
				ANS += X[1];
				if(ANS>HOLDER) HOLDER = ANS;
			}
			Console.WriteLine(HOLDER);

		}
	}
}
