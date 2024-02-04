#include <iostream>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        init();
        long long N, T, S=0;
        cin>>N;
        for(long long i=0; i<N; i++){
                cin>>T;
                S = S+T;
        }
        cout<<S-N+1<<'\n';
}
