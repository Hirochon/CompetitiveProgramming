#include <iostream>

int main() {
    int c[20] = {1,2,3,4,5,6,7,8,9,10};
    for (int i = 0; c[i] != '\0'; i++) {
        printf("%d\n", c[i]);
        printf("%p\n", c[i]);
    }
    int k = c[1];
    for (int i = 0; i < 5; i++) {
        printf("%d\n", k+i);
    }
    printf("%d", c[10]);
    return 0;
}