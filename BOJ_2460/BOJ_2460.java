import java.io.*;
import java.util.*;

class Main{
	public static void main(String[] args)
			throws IOException{
			BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
			int ANS = 0, HOLDER = 0;
			for(int i=0; i<10; i++){
				StringTokenizer ST = new StringTokenizer(BR.readLine());
				int N = Integer.parseInt(ST.nextToken());
				int M = Integer.parseInt(ST.nextToken());
				ANS -= N;
				ANS += M;
				if(ANS>HOLDER) HOLDER = ANS;

			}
			BW.write(HOLDER + "\n");
			BW.flush();


	}
}
