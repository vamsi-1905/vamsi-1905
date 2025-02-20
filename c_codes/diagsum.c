#include <stdio.h>

int main()
{
    int a[10][10],n,m,sum=0;

    printf("Enter dimensions n amd m:");
    scanf("%d %d",&n,&m);
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    printf("\nThe sum of diagonal elements are:\n");
     for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            if (i==j)
            {
                sum=sum+a[i][j];
            }
        }
    }
    printf("%d",sum);

}
