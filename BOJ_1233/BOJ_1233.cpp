#include <iostream>
using namespace std;
int main(){
        int A, B, C, HOLDER=0, LEAF;
        int ANS[100] = {0, };
        cin>>A>>B>>C;
        for(int i=1; i<=A; i++){
                for(int j=1; j<=B; j++){
                        for(int k=1; k<=C; k++){
                                ANS[i+j+k] += 1;
                        }
                }
        }
        for(int i=2; i<82; i++){
                if(HOLDER<ANS[i]){
                        HOLDER = ANS[i];
                        LEAF = i;
                }
        }
        cout<<LEAF<<'\n';
}
