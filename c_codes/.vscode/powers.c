#include<stdio.h>
int main(void)

{
    int power = 1,i,n,a;

    printf("What is a ?\n");
    scanf("%d", &a);

    printf("What is n ?\n");
    scanf("%d", &n);

    for(i = 1;i <= n;i++)
   {
    power = power*a;
   }
printf("%d", power);


}
