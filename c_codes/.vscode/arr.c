#include <stdio.h>
int main(void)
{
    int sum = 0, m, n, i, j;
    printf("What is m and n\t");
    scanf("%d%d", &m, &n);
    int a[m][n];
    printf("Enter elements of the array:\n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            sum = sum + a[i][j];
        }
    }
    printf("Sum of elements of array is %d\n", sum);
}
