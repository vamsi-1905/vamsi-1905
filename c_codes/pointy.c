#include<stdio.h>
int main(void)
{
    int a[10];
    int *p;
    p = a;
    int n;

    printf("What is n\t");
    scanf("%d",&n);

    for(int i=0;i<n;i++)
    {
        scanf("%d",p+i);
    }
  for(int i=0;i<n;i++)
  {
    printf("%d ",*(p+i));
  }
}
