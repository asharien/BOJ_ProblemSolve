#include <iostream>
using namespace std;
int main(){
        double A, B;
        cin >> A >> B;
        cout.setf(ios_base::fixed, ios_base::floatfield);
        cout.precision(12);
        cout << (long double)A/(long double)B << endl;
        return 0;
}
