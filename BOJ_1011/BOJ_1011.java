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
			long A = Long.parseLong(X[0]);
			long B = Long.parseLong(X[1]);
			SB.append(String.format("%.0f", Math.floor((Math.sqrt(4*(B-A)-1))))).append("\n");
		}
		BW.write(SB+"");
		BW.flush();
	}
}
