#include <stdio.h>

int main() {
    int N, k, i, n, l;
     printf("what is n\t");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("What is N\t");
        scanf("%d", &N);
        k = 1;
        l = N;
        while (k != l) {
                k++;
                l--;
        }
        printf("%d\n", k);
    }
}
