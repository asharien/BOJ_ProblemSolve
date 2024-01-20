#include <iostream>
#include <algorithm>
using namespace std;
int main(){
        int N;
        cin>>N;
        int *X = new int[N+1];
        for(int i=2; i<=N; i++){
                X[i] = X[i-1]+1;
                if(i%2 == 0) X[i] = min(X[i], X[i/2]+1);
                if(i%3 == 0) X[i] = min(X[i], X[i/3]+1);
        }
        cout<<X[N]<<'\n';
}
