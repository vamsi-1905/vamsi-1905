#include<stdio.h>

 int main(void)
{
int a , b;
 a = 2;
 b = 1;

switch(a||b)
{
    case 1 : printf("true");
    break;
    case 0 : printf("false");
    break;
}
}
