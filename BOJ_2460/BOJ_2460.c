#include <stdio.h>
int main(){
	int ANS = 0, HOLDER = 0;
	int N, M;
	for(int i=0; i<10; i++){
		scanf("%d %d", &N, &M);
		ANS -= N;
		ANS += M;
		if(ANS>HOLDER) HOLDER = ANS;
	}
	printf("%d\n", HOLDER);
	return 0;
}
