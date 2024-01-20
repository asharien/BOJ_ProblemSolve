#include <iostream>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        init();
        int N, HISTORY, F=1, S=1;
        int TP[51];
        cin>>N;
        for(int i=0; i<N; i++) cin>>TP[i];
        HISTORY=TP[0];
        for(int i=0; i<N; i++){
                if(TP[i]>HISTORY){
                        F+=1;
                        HISTORY = TP[i];
                }
        }
        HISTORY=TP[N-1];
        for(int i=N-1; i>=0; i--){
                if(TP[i]>HISTORY){
                        S+=1;
                        HISTORY = TP[i];
                }
        }
        cout<<F<<'\n'<<S<<'\n';
}
