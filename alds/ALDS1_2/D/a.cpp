#include <iostream>
#include <math.h>
using namespace std;
static const int MAX = 1000000;
int cnt = 0;

void insertionSort(int *A, int n, int g) {
    int v, j;
    for (int i = g; i < n; i++) {
        v = A[i];
        j = i - g;
        while (j >= 0 && A[j] > v) {
            A[j+g] = A[j];
            j = j - g;
            cnt++;
        }
        A[j+g] = v;
    }
}

void shellSort(int *A, int n) {
    int mod = n, modCnt=0;
    int G[MAX / 2];
    if (n == 1) {
        cout << 1 << endl << 1 << endl;
        return;
    }

    for (int i = 0;; i++) {
        mod = floor(mod / 3);
        if (mod < 3) {
            G[modCnt] = 1;
            modCnt++;
            break;
        }
        G[i] = mod;
        modCnt++;
    }
    cout << modCnt << endl;

    for (int i = 0; i < modCnt; i++) {
        if (i) cout << ' ';
        cout << G[i];
    }
    cout << endl;

    for (int i = 0; i < modCnt; i++) {
        insertionSort(A, n, G[i]);
    }
}

int main() {
    int n, A[MAX];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> A[i];
    shellSort(A, n);
    cout << cnt << endl;
    for (int i = 0; i < n; i++) {
        cout << A[i] << endl;
    }
    return 0;
}