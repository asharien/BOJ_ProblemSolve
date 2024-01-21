#include <iostream>
#include <algorithm>
using namespace std;
void init(){
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(false);
}
int main(){
	init();
	int CASE, N, CARL=0, FLAG=false;
	int VOTE[1000001];
	cin>>CASE;
	for(int i=0; i<CASE; i++){
		cin>>VOTE[i];
	}
	string ANS = (VOTE[0]>=*max_element(VOTE, VOTE + CASE))? "S":"N";
	cout<<ANS<<"\n";
}
