#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a;
    a = 4 / 3;
    cout << a << endl;

    vector<int> b;
    b.push_back(2);    
    b.push_back(4);    
    b.push_back(6);    
    b.push_back(9);

    cout << b[2] << endl;

    return 0;
}