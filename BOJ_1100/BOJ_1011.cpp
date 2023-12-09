#include <iostream>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        init();
        char L[10];
        int C=0;
        for(int i=0; i<8; i++){
                for(int j=0; j<8; j++){
                        cin>>L[j];
                        if(i%2==0 &&j%2==0 && L[j]=='F')C++;
                        else if(i%2!=0&&j%2!=0&&L[j]=='F')C++;
                }

        }
        cout<<C<<'\n';
}
