#include<stdio.h>

int main(void)
{
    int b,a,c,D;

printf("Enter b: ");
scanf("%d", &b);

printf("Enter c: ");
scanf("%d", &c);

printf("Enter a: ");
scanf("%d", &a);

D = (b*b)-4*a*c;

printf("Discriminant is equal to: %d\n", D);

return 0;
}
