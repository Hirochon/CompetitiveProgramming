#include <iostream>
using namespace std;
static const int MAX = 100;

int main() {
    int n, j, tmp;
    int A[MAX];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int k = 0; k < n; k++) {
        if (k != n-1) {
            printf("%d ", A[k]);
        } 
        else {
            printf("%d\n", A[k]);
        }
    }
    for (int i = 1; i < n; i++) {
        j = i - 1;
        while (j >= 0 && A[j] > A[j+1]) {
            tmp = A[j+1];
            A[j+1] = A[j];
            A[j] = tmp;
            j--;
        }
        for (int k = 0; k < n; k++) {
            if (k != n-1) {
                printf("%d ", A[k]);
            } 
            else {
                printf("%d\n", A[k]);
            }
        }
    }
    return 0;
}