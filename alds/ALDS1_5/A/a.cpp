#include <iostream>
#include <vector>
using namespace std;
#define r(i, n) for(int i = 0; i < n; i++)

int n;

bool solve(int A[], int b, int m) {
    bool res;
    if (b == 0) return true;
    else if (n < m+1) return false;
    else if (b < 0) return false;
    res = solve(A, b, m+1) | solve(A, b - A[m], m+1);
    return res;
}

int main() {
    int q, a, b;
    int A[22], B[202];
    scanf("%d", &n);
    r(i, n) {
        scanf("%d", &a);
        A[i] = a;
    }
    scanf("%d", &q);
    r(i, q) {
        scanf("%d", &b);
        B[i] = b;
    }

    r(i, q) {
        if(solve(A, B[i], 0)) {
            printf("yes\n");
        }
        else {
            printf("no\n");
        }
    }

    return 0;
}