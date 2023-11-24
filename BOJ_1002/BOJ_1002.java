import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.math.*;
class Main {
	public static void main(String[] args) 
	throws IOException{
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder SB =  new StringBuilder();
		int N = Integer.parseInt(BR.readLine());
		for(int i=0; i<N; i++){
			String[] X = BR.readLine().split(" ");
			int X1 = Integer.parseInt(X[0]); int Y1 = Integer.parseInt(X[1]); int R1 = Integer.parseInt(X[2]);
			int X2 = Integer.parseInt(X[3]); int Y2 = Integer.parseInt(X[4]); int R2 = Integer.parseInt(X[5]);
			double D = Math.sqrt(Math.pow((X1-X2),2) + Math.pow((Y1-Y2),2));
			String ANS = ((X1==X2 && Y1 == Y2 && R1 == R2))?"-1":((X1==X2 && Y1==Y2) && R1 != R2)?"0":((R1+R2 == D) || (Math.abs(R1-R2) == D))? "1":(Math.abs(R1-R2)<D && D<R1+R2)? "2":"0";
		SB.append(ANS).append("\n");
		}
		BW.write(SB+"");
		BW.flush();
	}
}
