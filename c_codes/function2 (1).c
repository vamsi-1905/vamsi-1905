#include<stdio.h>
 int add(void);
 int main()
{
    int c;
    c = add();
    printf("%d",c);
}
    int add()
{
    int a,b,c;
    scanf("%d%d",&a,&b);
    c = a+b;
    return c;

}
