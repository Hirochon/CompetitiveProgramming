#include<stdio.h>
#include <string.h>

int main(void){
    int K, flag, flag2, len;
    int i, j;
    char mozi[50];
    scanf("%d", &K);
    if (K <= 12){
        printf("%d", K);
    }
    else {
        i = flag = 12;
        while(K != flag){
            i++;
            sprintf(mozi, "%d", i);
            len = strlen(mozi);
            flag2 = 0;
            for (j = 0; j < len-1; j++){
                if ((mozi[j] == mozi[j+1]) || (mozi[j]+1 == mozi[j+1]) || (mozi[j]-1 == mozi[j+1])){
                    flag2 += 1;
                    continue;
                }
                else{
                    break;
                }
            }
            if (flag2 == len-1){
                flag += 1;
            }
        }
        printf("%d\n", i);
    }
    return 0;
}