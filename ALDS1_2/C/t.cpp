#include <iostream>
#include <string>
#include <vector>
using namespace std;
static const int MAX = 36;

int bubbleSort(vector<string> &A, int N) {
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

int selectionSort(vector<string> &A, int N) {
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

bool isStable(vector<string> &A, vector<string> &B, int N) {
    for (int i = 0; i < N; i++) {
        if (A[i][1] != B[i][1] || A[i][0] != B[i][0]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    string t;
    vector<string> arr1, arr2;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> t;
        arr1.push_back(t);
        arr2.push_back(t);
    }

    bubbleSort(arr1, n);
    selectionSort(arr2, n);

    for (int i = 0; i < n; i++) {
        // if (i) cout << " ";
        cout << arr1[i];
        if (i != n-1) {
            cout << " ";
        }
    }
    cout << endl;
    cout << "Stable" << endl;

    for (int i = 0; i < n; i++) {
        // if (i) cout << " ";
        cout << arr2[i];
        if (i != n-1) {
            cout << " ";
        }
    }
    cout << endl;
    if (!isStable(arr1, arr2, n)) {
        cout << "Not stable" << endl;
    }
    else {
        cout << "Stable" << endl;
    }

    return 0;
}