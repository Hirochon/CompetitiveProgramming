#include <iostream>
#define r(i, n) for (int i = 0; i < n; i++)
using namespace std;

int main() {
    int n, q, s, ans=0;
    int S[10005];
    cin >> n;
    r(i, n) {
        cin >> S[i];
    }
    cin >> q;
    r(i, q) {
        cin >> s;
        r(j, n) {
            if (S[j] == s) {
                ans++;
                break;
            }
        }
    }
    cout << ans << endl;
    return 0;
}