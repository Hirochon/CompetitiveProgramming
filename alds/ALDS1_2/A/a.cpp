#include <iostream>
using namespace std;
static const int MAX = 100;

void callList(int *A, int N) {
    for (int i = 0; i < N; i++) {
        if (i) cout << " ";
        cout << A[i];
    }
    cout << endl;
}

int bubbleSort(int *A, int N) {
    int swapNum = 0;
    int tmp;
    for (int j = N-1; j > 0; j--) {
        for (int i = N-1; i > N-j-1; i--) {
            if (A[i] < A[i-1]) {
                tmp = A[i];
                A[i] = A[i-1];
                A[i-1] = tmp;
                swapNum++;
            }
        }
    }
    return swapNum;
}

int main() {
    int N, A[MAX], swapNum;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    swapNum = bubbleSort(A, N);
    callList(A, N);
    cout << swapNum << endl;
    return 0;
}