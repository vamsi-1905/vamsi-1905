#include <stdio.h>
int main(void)
{
     int n, m;
    int sum = 0;
    int count = 0;

    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int a[50][50];

    printf("Enter the elements of the array:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            m = a[i][j];
            if (m != 0) {
                count = 0;
                for (int k = 0; k < n; k++) {
                    for (int l = 0; l < n; l++) {
                        if (a[k][l] == m) {
                            count++;
                            a[k][l] = 0;
                        }
                    }
                }
                printf("The frequency of the element %d is %d\n", m, count);
            }
        }
    }
}
