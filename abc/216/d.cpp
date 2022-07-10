#include <iostream>
#include <list>
#define r(i, n) for(int i = 0; i < n; i++)
using namespace std;

int main() {
    int N, M;
    list<int> Q[200006];
    int T[200006];

    scanf("%d %d", &N, &M);
    r(i, M) {
        r(j, N) {
            int a;
            scanf("%d", &a);
            Q[i].push_back(a);
        }
    }
    r(i, M) {
        r(j, N) {
            printf("%d ", Q[i].front());
            Q[i].pop_front();
        }
        printf("\n");
    }
    return 0;
}