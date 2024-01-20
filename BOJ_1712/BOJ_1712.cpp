#include <iostream>
using namespace std;
int main(){
        int A, B, C;
        cin>>A>>B>>C;
        double ANS = (B>=C)? -1:A/(C-B)+1;
        cout<<fixed;
        cout.precision(0);
        cout<<ANS<<'\n';
}
