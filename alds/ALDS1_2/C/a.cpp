#include <iostream>
using namespace std;
static const int MAX = 36;

int bubbleSort(char A[MAX][3], int N) {
    int swapNum = 0;
    int tmp1, tmp2;
    for (int j = N-1; j > 0; j--) {
        for (int i = N-1; i > N-j-1; i--) {
            tmp1 = int(A[i][1]);
            tmp2 = int(A[i-1][1]);
            if (tmp1 < tmp2) {
                swap(A[i], A[i-1]);
                swapNum++;
            }
        }
    }
    return swapNum;
}

int selectionSort(char A[MAX][3], int N) {
    int swapNum = 0;
    int minj, tmp1, tmp2;
    for (int i = 0; i < N; i++) {
        minj = i;
        for (int j = minj; j < N; j++) {
            tmp1 = A[j][1];
            tmp2 = A[minj][1];
            if (tmp1 < tmp2) {
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

bool isStable(char A[MAX][3], char B[MAX][3], int N) {
    for (int i = 0; i < N; i++) {
        if (A[i][1] != B[i][1] || A[i][0] != B[i][0]) {
            return false;
        }
    }
    return true;
}

int main() {
    int N;
    char A[MAX][3], B[MAX][3];
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        for (int j = 0; j < 2; j++) {
            B[i][j] = A[i][j];
        }
    }

    bubbleSort(A, N);
    selectionSort(B, N);

    for (int i = 0; i < N; i++) {
        cout << A[i];
        if (i != N-1) {
            cout << " ";
        }
    }
    cout << endl;
    cout << "Stable" << endl;

    for (int i = 0; i < N; i++) {
        cout << B[i];
        if (i != N-1) {
            cout << " ";
        }
    }
    cout << endl;
    if (!isStable(A, B, N)) {
        cout << "Not stable" << endl;
    }
    else {
        cout << "Stable" << endl;
    }

    return 0;
}