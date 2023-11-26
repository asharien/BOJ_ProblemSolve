#include <iostream>
#include <queue>
using namespace std;
void init(){
        cin.tie(0);
        cout.tie(0);
        ios_base::sync_with_stdio(false);
}
int main(){
        init();
        int A, B, CASE, TEMP, TEMP2;
        int PATTERNS[10][10] = {{10}, {1}, {2,4,8,6}, {3, 9, 7,1}, {4, 6}, {5}, {6}, {7, 9, 3, 1}, {8,4,2,6}, {9, 1}};
        cin>> CASE;
        for(int i=0; i<CASE; i++){
                cin>> TEMP >> TEMP2;
                A = TEMP%10;
                switch (A){
                        case 0:
                                B = 1;
                                break;
                        case 1:
                                B = 1;
                                break;
                        case 2:
                                B = TEMP2%4;
                                if(B == 0){
                                        B = 4;
                                }
                                break;
                        case 3:
                                B = TEMP2%4;
                                if(B == 0){
                                        B = 4;
                                }
                                break;
                        case 4:
                                B = TEMP2%2;
                                if(B == 0){
                                        B = 2;
                                }
                                break;
                        case 5:
                                B = 1;
                                break;
                        case 6:
                                B = 1;
                                break;
                        case 7:
                                B = TEMP2%4;
                                if(B == 0){
                                        B = 4;
                                }

                                break;
                        case 8:
                                B = TEMP2%4;
                                if(B == 0){
                                        B = 4;
                                }
                                break;
                        case 9:
                                B = TEMP2%2;
                                if(B == 0){
                                        B = 2;
                                }
                                break;
                        default:
                                break;

                }
                cout<< PATTERNS[A][B-1] << '\n';
        }

        return 0;
}
