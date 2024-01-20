#include <iostream>
using namespace std;
int main(){
        int N;
        int BOX[101];
        cin>>N;
        for(int i=0; i<N; i++){
                cin>>BOX[i];
        }
        if(BOX[2]-BOX[1] == BOX[1]-BOX[0]) cout<<BOX[N-1]+(BOX[1]-BOX[0])<<'\n';
        else if(BOX[2]/BOX[1] == BOX[1]/BOX[0]) cout<<BOX[N-1]*(BOX[1]/BOX[0])<<'\n';
}
