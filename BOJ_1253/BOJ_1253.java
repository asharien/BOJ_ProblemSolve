import java.io.*;
import java.util.*;
import java.util.stream.LongStream;

class Main{
	public static void main(String[] args)
			throws IOException{
			BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
			long N = Long.parseLong(BR.readLine());
			String[] X = BR.readLine().split(" ");
			long[] L = Arrays.stream(X).mapToLong(Long::parseLong).toArray();
			Arrays.sort(L);
			int ANS=0;
			for(int i=0; i<N; i++){
				long TARGET = L[i];
				long[] TMP = new long[L.length -1];
				int UP=0, DW=TMP.length-1;
				for(int j=0, CNT=0; j<L.length-1; j++){
					if(j==i) {
						TMP[j] = L[CNT+1];
						CNT +=2;
					}
					else {
						TMP[j]=L[CNT];
						CNT +=1;
					}
				}
				while(UP<DW){
					long S = TMP[UP]+TMP[DW];
					if(S<TARGET) UP += 1;
					else if(S>TARGET) DW -=1;
					else{
						ANS +=1;
						UP +=1;
						DW -=1;
						break;
					}
				}

			}
			BW.write(ANS+"\n");
			BW.flush();


	}
}
