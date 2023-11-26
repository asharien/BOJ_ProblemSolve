#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int A, B, CASE;
	int DATA[1000];
	scanf("%d", &CASE);
	for (int i = 0; i < CASE; i++) {
		scanf("%d %d", &A, &B);
		DATA[i] = 1;
		for (int j = 0; j < B; j++) {
			DATA[i] = DATA[i] * (A % 10);
			DATA[i] = DATA[i] % 10;
		}
	}
	for (int i = 0; i < CASE; i++) {
		if (DATA[i] == 0) {
			printf("10\n");
		}
		else {
			printf("%d\n", DATA[i]);
		}
	}
	return 0;
}
