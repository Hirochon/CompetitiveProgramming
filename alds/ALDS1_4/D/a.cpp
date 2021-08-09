#include <iostream>
using namespace std;
#define MAX 100000
#define r(i, n) for(int i = 0; i < n; i++)
typedef long long llong;

int n, k;
llong T[MAX];

int check(llong P) {
    int i = 0;
    r(j, k) {
        llong s = 0;
        while(s + T[i] <= P) {
            s += T[i];
            i++;
            if (i == n) return n;
        }
    }
    return i;
}

int solve() {
    llong left = 0;
    llong right = MAX * 10000;
    llong mid;
    while(right - left > 1) {
        mid = (left + right) / 2;
        int v = check(mid);
        if (v >= n) right = mid;
        else left = mid;
    }
    return right;
}

int main() {
    cin >> n >> k;
    r(i, n) cin >> T[i];
    llong ans = solve();
    cout << ans << endl;
}