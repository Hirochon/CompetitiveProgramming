#include <iostream>
#include <list>
using namespace std;
static const int MAX = 1000000;

int main() {
    int n, num = 0, cInt;
    char cStr[20];
    list<int> numList;
    list<int>::iterator it1, it2;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", cStr);

        if (cStr[6] == '\0') {
            scanf("%d", &cInt);

            if (cStr[0] == 'i') {
                numList.push_front(cInt);
            }
            else if (cStr[0] == 'd') {
                for (it1 = numList.begin(); it1 != numList.end(); ++it1) {
                    if (*it1 == cInt) {
                        it1 = numList.erase(it1);
                        break;
                    }
                }
            }
        }

        else {
            if (cStr[6] == 'F') {
                numList.pop_front();
            }
            else if (cStr[6] == 'L') {
                numList.pop_back();
            }
        }
    }
    for(int i = 0; !numList.empty(); i++) {
        if (i) printf(" ");
        cout << numList.front();
        numList.pop_front();
    }
    printf("\n");
    return 0;
}