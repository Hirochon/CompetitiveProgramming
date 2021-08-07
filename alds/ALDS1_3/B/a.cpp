#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n, q, cost=0;
    cin >> n >> q;
    queue<int> Q;
    queue<string> S;
    for (int i = 0; i < n; i++) {
        string name;
        int time;
        cin >> name >> time;
        Q.push(time);
        S.push(name);
    }
    while (!Q.empty()) {
        int t = Q.front();
        if (q >= t) {
            cout << S.front() << " " << cost + t << endl;
            Q.pop();
            S.pop();
            cost += t;
        }
        else {
            Q.push(t - q);
            S.push(S.front());
            Q.pop();
            S.pop();
            cost += q;
        }
    }
    return 0;
}