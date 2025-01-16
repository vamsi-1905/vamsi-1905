#include<stdio.h>
int power(int a ,int n);
int main()
{ int n,a;
    printf("What is n,a\t");
    scanf("%d%d",&n,&a);
   int result = power(a,n);
    printf("%d^%d=%d",a,n,result);

}
int power(int a , int n)
{
    if(n==1)
    return a;
    else
    return a*power(a,n-1);
}
