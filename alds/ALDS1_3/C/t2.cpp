#include <iostream>

int main() {
    char s[20];
    int k;
    scanf("%s", s);
    if (scanf("%d", &k) != EOF) printf("%s\n%d\n", s, k);
    else printf("%s\n", s);
    return 0;
}