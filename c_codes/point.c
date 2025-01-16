#include<stdio.h>
int main(void)
{
int a = 10;
int *p,c;
p = &a;
c = sizeof(p);
printf("%d",c);
}
