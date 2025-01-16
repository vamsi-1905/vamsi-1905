#include<stdio.h>
int fact(int in);
int main()
{ int n;
    printf("What is n\t");
    scanf("%d",&n);
   int x = fact(n);
    printf("%d",x);

}
int fact(int n)
{
    if(n==1)
    return 1;
    else
    return n*fact(n-1);
}


