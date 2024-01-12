#include <iostream>
using namespace std;
int main(){
        int N, M, SEQUENCE=0, HWOOD=0, VWOOD=0;
        char FLOOR[100][100];
        char VERT = '|';
        char FLAT = '-';
        cin>>N>>M;
        for(int i=0; i<N; i++){
                cin>>FLOOR[i];
        }
        for(int i=0; i<N; i++){
                for(int j=0; j<M; j++){
                        if(FLOOR[i][j] == FLAT) SEQUENCE = 1;
                        else if(FLOOR[i][j] == VERT && SEQUENCE == 1){
                                HWOOD++;
                                SEQUENCE = 0;
                        }
                        else continue;
                }
                HWOOD = HWOOD + SEQUENCE;
                SEQUENCE = 0;
        }
        SEQUENCE = 0;
        for(int i=0; i<M; i++){
                for(int j=0; j<N; j++){
                        if(FLOOR[j][i] == VERT) SEQUENCE = 1;
                        else if(FLOOR[j][i] == FLAT && SEQUENCE == 1){
                                VWOOD++;
                                SEQUENCE = 0;
                        }
                        else continue;
                }
                VWOOD = VWOOD + SEQUENCE;
                SEQUENCE = 0;
        }
        cout<<VWOOD+HWOOD<<'\n';
}
