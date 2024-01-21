#include <stdio.h>
#include <stdbool.h>
int main(){
	int CASE, N, CARL=0, FLAG=false;
	int CAND[100001];
	scanf("%d", &CASE);
	for(int i=0; i<CASE; i++){
		scanf("%d", &N);
		CAND[i] = N;
		if(i==0) CARL = N;
		if(CARL<N) FLAG =true;

	}
	printf("%s\n", FLAG? "N":"S");
	return 0;
}
