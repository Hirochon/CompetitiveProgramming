#include <iostream>
#include <algorithm>
#include <vector>
#define r(i, init, n) for (int i = init; i < n; i++)
using namespace std;

bool binarySerch(vector<int> S, int m) {
    int start = 0;
    int end = S.size();
    int num, check;
    while(1) {
        num = (end - start) / 2 + start;
        check = S[num];
        if (m == check) {
            return true;
        }
        else if (end - start == 1) {
            return false;
        }
        else if (m < check) {
            end = num;
        }
        else {
            start = num;
        }
    }
}

int main() {
    int n, q, s, ans=0, v;
    vector<int> S;
    cin >> n;
    r(i, 0, n) {
        cin >> v;
        S.push_back(v);
    }
    sort(begin(S), end(S));
    cin >> q;
    r(i, 0, q) {
        cin >> s;
        if(binarySerch(S, s)) {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}