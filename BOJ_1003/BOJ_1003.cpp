#include <iostream>

using namespace std;
int RECOLLECT[50];

int FIBONACCI(int RECALL);


int main(){
        int N, CASE;
        cin>> CASE;
        for(int i; i<CASE; i++){
                cin>>N;
                if(N == 0){
                        cout<<"1 0\n";
                }
                else if(N == 1){
                        cout<<"0 1\n";
                }
                else if(N == 2){
                        cout<<"1 1\n";
                }
                else{
                        FIBONACCI(N);
                        cout<<RECOLLECT[N-1]<<" "<<RECOLLECT[N]<<endl;
                }
        }

        return 0;
}
int FIBONACCI(int RECALL){
        if(RECALL <= 0){
                RECOLLECT[0] = 0;
                return 0;
        }
        else if(RECALL == 1){
                RECOLLECT[1] = 1;
                return 1;
        }
        if(RECOLLECT[RECALL] != 0){
                return RECOLLECT[RECALL];
        }
        else{
                RECOLLECT[RECALL] = FIBONACCI(RECALL-1) + FIBONACCI(RECALL-2);
                return RECOLLECT[RECALL];
        }
}
