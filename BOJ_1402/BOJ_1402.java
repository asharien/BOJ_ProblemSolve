import java.io.*;
import java.util.*;
import java.math.BigInteger;
class Main {
	public static void main(String[] args) 
	throws IOException{
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder SB = new StringBuilder();
		int testCases = Integer.parseInt(BR.readLine());
        	for(int i=0; i<testCases; i++){
			StringTokenizer ST = new StringTokenizer(BR.readLine());
			BigInteger A = new BigInteger(ST.nextToken());
			BigInteger B = new BigInteger(ST.nextToken());
			if(A.compareTo(B)>=-1){
				SB.append("yes\n");
			}
			else{
				SB.append("no\n");
			}
		}
		BW.write(SB+"");
		BW.flush();
	}
}
