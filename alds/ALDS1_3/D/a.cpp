#include <iostream>
#include <stack>
#define r(i, n) for(int i = 0; n; i++)
using namespace std;
static const int MAX = 20002;

int main() {
    char c;
    int kudari[MAX], nobori[MAX], ans[MAX];
    stack<int> S1;
    int k, k1, k2, length=0, partSum=0, sum=0, sumNum=0, flagSum=0;
    r(i, cin >> c) {
        length++;
        // printf("%d %c\n", i, c);
        if (c == '\\') S1.push(i);
        else if (c == '/') {
            if (S1.empty()) continue;

            k1 = S1.top();
            S1.pop();
            k2 = i;
            k = k2 - k1;
            kudari[k1] = k;
            nobori[k2] = k;
        }
    }
    int j=0;
    r(i, i < length) {
        partSum += kudari[i];
        flagSum += kudari[i];
        flagSum -= nobori[i];
        // cout << i << partSum << flagSum << endl;
        if (flagSum == 0) {
            if(partSum) {
                sum += partSum;
                sumNum++;
                ans[j] = partSum;
                j++;
                partSum = 0;
            }
        }
    }
    cout << sum << endl;
    cout << sumNum;
    r(i, i < sumNum) {
        cout << ' ' << ans[i];
    }
    cout << endl;
    return 0;
}