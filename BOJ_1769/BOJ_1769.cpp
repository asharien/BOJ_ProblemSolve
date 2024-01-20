#include <iostream>
#include <string>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        string X;
        int ANS =0;
        int TMP=0, TMP2=0, CNT=0;
        cin>>X;
        int L = X.length();
        for(int i=0; i<L; i++){
                ANS += (int)X[i]-48;
        }
        while(ANS/10 != 0){
                TMP = ANS;
                while(TMP !=0){
                        TMP2 += TMP%10;
                        TMP = TMP/10;
                }
                ANS = TMP2;
                CNT++;
                TMP2 =0;
        }
        CNT = (L>1)?CNT+1:CNT;
        string YENO = (ANS%3 == 0)?"YES":"NO";
        cout<<CNT<<'\n'<<YENO<<'\n';
}
