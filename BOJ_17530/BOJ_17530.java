import java.io.*;
import java.util.*;

class Main{
	public static void main(String[] args)
			throws IOException{
			BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
			int CASE = Integer.parseInt(BR.readLine());
			int[] VOTE = new int[CASE];
			for(int i=0; i<CASE; i++) VOTE[i] = Integer.parseInt(BR.readLine());
			String ANS = (VOTE[0]>=Arrays.stream(VOTE).max().getAsInt()? "S":"N");
			BW.write(ANS+"\n");
			BW.flush();
	}
}
