#include <iostream>
using namespace std;
void init(){
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);
}
int main(){
	init();
	int ANS = 0, HOLDER = 0;
	int N, M;
	for(int i=0; i<10; i++){
		cin>>N>>M;
		ANS -=N;
		ANS +=M;
		if(ANS>HOLDER) HOLDER = ANS;
	}
	cout <<HOLDER<<"\n";
	return 0;
}
