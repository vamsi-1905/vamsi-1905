#include<stdio.h>
int power(int,int);
int main(void)
{
    int a , b ,p;
    printf("What is a and what is n: ");
    scanf("%d %d" ,&a ,&b);
    p = power(a , b);
    printf("%d",p);
}
int power(int a , int b)
{
    int p =1 , i;
    for( i=1;i<=b;i++)
    {
        p = p*a;

    }
    return p;
}
