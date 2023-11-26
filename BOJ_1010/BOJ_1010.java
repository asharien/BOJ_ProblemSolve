import java.io.*;
import java.util.*;
import java.math.BigInteger;
class Main {
	public static void main(String[] args) 
	throws IOException{
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter BW = new BufferedWriter(new OutputStreamWriter(System.out));
		//StringBuilder SB = new StringBuilder();
		int testCases = Integer.parseInt(BR.readLine());

        for (int t = 0; t < testCases; t++) {
            String[] input = BR.readLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);
            BigInteger result = calculateCoefficient(N, M);
            BW.write(result + "\n");
			BW.flush();
        }
    }
    static BigInteger calculateCoefficient(int n, int m) {
        BigInteger numerator = calculateFactorial(m);
        BigInteger denominator = calculateFactorial(m - n).multiply(calculateFactorial(n));
        return numerator.divide(denominator);
    }

    static BigInteger calculateFactorial(int num) {
        if (num == 0 || num == 1) {
            return BigInteger.ONE;
        } else {
            BigInteger result = BigInteger.ONE;
            for (int i = 2; i <= num; i++) {
                result = result.multiply(BigInteger.valueOf(i));
            }
            return result;
        }
	}
}
