#include <iostream>
static const int MAX = 1000000;

bool judgeChar(char *cStr, const char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (cStr[i] != s[i]) {
            return false;
        }
    }
    return true;
}

int insertList(int *list, int n, int num) {
    list[num] = n;
    return num + 1;
}

int deleteList(int *list, int n, int num) {
    for (int i = num-1; i >= 0; i--) {
        if (list[i] == n) {
            for (int j = i; j < num; j++) {
                list[j] = list[j+1];
            }
            return num - 1;
        }
    }
    return num;
}

int deleteLastList(int *list, int num) {
    for (int i = 1; i < num; i++) {
        list[i-1] = list[i];
    }
    list[num-1] = '\0';
    return num - 1;
}

int deleteFirstList(int *list, int num) {
    list[num-1] = list[num];
    return num - 1;
}

int main() {
    int n, num = 0, cInt;
    char cStr[20];
    int list[MAX];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s", cStr);

        if (cStr[6] == '\0') {
            scanf("%d", &cInt);

            if (judgeChar(cStr, "insert")) {
                num = insertList(list, cInt, num);
            }
            else if (judgeChar(cStr, "delete")) {
                num = deleteList(list, cInt, num);
            }
        }

        else {
            if (judgeChar(cStr, "deleteFirst")) {
                num = deleteFirstList(list, num);
            }
            else if (judgeChar(cStr, "deleteLast")) {
                num = deleteLastList(list, num);
            }
        }

        // for(int i = num-1; i >= 0; i--) {
        //     if (num - 1 != i) printf(" ");
        //     printf("%d", list[i]);
        // }
        // printf("\n");
    }
    for(int i = num-1; i >= 0; i--) {
        if (num - 1 != i) printf(" ");
        printf("%d", list[i]);
    }
    printf("\n");
    return 0;
}