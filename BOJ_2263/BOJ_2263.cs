using System;
using System.Linq;
using System.Text;
namespace asharien{
        public class PROGRAM{
                static StringBuilder SB = new StringBuilder();
                static int[] TREE;
                static int[] IN;
                static int[] POST;
                public static void Main(){
                        int N = int.Parse(Console.ReadLine());
                        IN = Console.ReadLine().Split().Select(int.Parse).ToArray();
                        POST = Console.ReadLine().Split().Select(int.Parse).ToArray();
                        TREE = new int[100001];
                        for(int i=0; i<N; i++) TREE[IN[i]] = i;
                        PRE(0, N-1, 0, N-1);
                        Console.WriteLine(SB);
                }
                public static void PRE(int INS, int INE, int POST_S, int POST_E){
                        if(INS>INE && POST_S>POST_E) return;
                        int ROOT = POST[POST_E];
                        int LEFT = TREE[ROOT] - INS;
                        int RIGHT = INE - TREE[ROOT];
                        SB.Append(ROOT).Append(" ");
                        PRE(INS, INS+LEFT-1, POST_S, POST_S+LEFT-1);
                        PRE(INE-RIGHT+1, INE, POST_E-RIGHT, POST_E -1);
                }
        }
}
