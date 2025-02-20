#include<stdio.h>
int main(void) {

    int n;
    
    scanf("%d", &n);

    int a[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            printf("%d ", a[i][j]);
        }
    }
    printf("\n");

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            printf("%d ", a[i][j]);
        }
    }
}
