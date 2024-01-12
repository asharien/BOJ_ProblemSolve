import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) 
	throws IOException{
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder SB = new StringBuilder();
		String[] XY = BR.readLine().split(" ");
		int X = FLIP(Integer.toString(FLIP(XY[0])+FLIP(XY[1])));
		BW.write(X+"\n");
		BW.flush();
	}
	public static int FLIP(String S){
		StringBuffer TEMP = new StringBuffer(S);
		String ANS = TEMP.reverse().toString();
		int REINT = Integer.parseInt(ANS);
		return REINT;
	}
}
