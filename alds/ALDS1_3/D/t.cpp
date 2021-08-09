#include <iostream>
#include <cmath>
#define r(i, n) for (int i = 0; i < n; i++)
using namespace std;
static const int MAX = 20000;

int main() {
    int a[MAX];
    a[2] = 3;
    a[1] = 4;

    r(i, 10) {
        printf("%d\n", a[i]);
    }
}