#include <iostream>
using namespace std;
int main(){
        int A, B, CNT =0, i=0;
        int CSUM[1024] = {0, };
        cin>>A>>B;
        while(1){
                i++;
                for(int j=0; j<i; j++){
                        if(CNT == B+1) break;
                        CSUM[CNT+1] = CSUM[CNT]+i;
                        CNT++;
                }
                if(CNT == B+1) break;
        }
        cout<<CSUM[B]-CSUM[A-1]<<'\n';
}
