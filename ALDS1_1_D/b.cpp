#include <iostream>
#include <algorithm>
using namespace std;
static const int MAX = 200000;

int main() {
    int R[MAX], n;

    cin >> n;
    cin >> R[0];
    
    int minNum = R[0];
    int maxNum = -2000000000;

    for (int i = 1; i < n; i++) {
        cin >> R[i];
        maxNum = max(maxNum, R[i] - minNum);
        minNum = min(minNum, R[i]);
    }
    cout << maxNum << endl;
    return 0;
}