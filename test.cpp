#include "stdio.h"
int main(int argc, char const *argv[]) {
    int n,a[50005];
    scanf("%d", &n);
    for (int i = 0; i < count; i++) {
        scanf("%d", &a[i]);
    }

    int flag_temp = 0, sum_temp = 0;

    for(int i = 0 ; i < n ; i++){
        int sum = 0,flag = 0;

        for (j = 0; j < n-i; j++) {
            sum = sum + a[i+j];
            flag ++;
            if(sum%7==0 && flag > flag_temp){
                flag_temp = flag;
            }
        }
    }
    printf("%d\n", flag_temp);
    return 0;
}
