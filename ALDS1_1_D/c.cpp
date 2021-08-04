#include <iostream>
#include <algorithm>
using namespace std;
static const int MAX = 200000;

int main() {
    int n, R[MAX], ans, minNum;

    cin >> n;
    cin >> R[0];
    ans = -2000000000;
    minNum = R[0];

    for (int i = 1; i < n; i++) {
        cin >> R[n];
        ans = max(ans, R[n] - minNum);
        if (minNum > R[n]) {
            minNum = R[n];
        }
    }

    cout << ans << endl;

    return 0;
}