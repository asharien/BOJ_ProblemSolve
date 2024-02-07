#include <iostream>
using namespace std;
int IN[100001], POST[100001], TABLE[100001];
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
void RETRACK(int INS, int INE, int POST_S, int POST_E){
        if(INS>INE && POST_S>POST_E) return;
        int ROOT = POST[POST_E];
        int LEFT = TABLE[ROOT]-INS;
        int RIGHT = INE - TABLE[ROOT];
        cout<<ROOT<<" ";
        RETRACK(INS, INS+LEFT-1, POST_S, POST_S+LEFT-1);
        RETRACK(INE-RIGHT+1, INE, POST_E-RIGHT, POST_E-1);
}
int main(){
        init();
        int N;
        cin>>N;
        for(int i=0; i<N; i++){
                cin>>IN[i];
                TABLE[IN[i]]=i;
        }
        for(int i=0; i<N; i++){
                cin>>POST[i];
        }
        RETRACK(0, N-1, 0, N-1);
        cout<<"\n";
}
