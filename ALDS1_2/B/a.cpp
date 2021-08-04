#include <iostream>
using namespace std;
static const int MAX = 100;

int selectionSort(int *A, int N) {
    int swapNum = 0;
    int minj;

    for (int i = 0; i < N; i++) {
        minj = i;
        for (int j = minj; j < N; j++) {
            if (A[j] < A[minj]) {
                minj = j;
            }
        }
        if (minj != i) {
            swap(A[i], A[minj]);
            swapNum++;
        }
    }

    return swapNum;
}

int main() {
    int A[MAX], N, swapNum;
    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];
    swapNum = selectionSort(A, N);
    for (int i = 0; i < N; i++) {
        if (i) cout << " ";
        cout << A[i];
    }
    cout << endl;
    cout << swapNum << endl;
    return 0;
}