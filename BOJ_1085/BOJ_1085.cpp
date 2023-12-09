#include <iostream>
#include <algorithm>

using namespace std;

int main(){
        int X, Y, W, H, BORDER_X, BORDER_Y, PLACE_HOLDER;
        cin>>X>>Y>>W>>H;
        BORDER_X = W-X;
        BORDER_Y = H-Y;
        PLACE_HOLDER = min(X,Y);
        PLACE_HOLDER = min(PLACE_HOLDER, BORDER_X);
        PLACE_HOLDER = min(PLACE_HOLDER, BORDER_Y);
        cout<<PLACE_HOLDER<<endl;
        return 0;
}
