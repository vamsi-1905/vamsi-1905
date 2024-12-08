#include<stdio.h>
int main(void)
{
int n,reversednum=0,remainder;

printf("Enter value: \n");
scanf("%d" , &n);

while(n!=0)
{
    remainder = n % 10;
    reversednum = reversednum*10 + remainder;
    n /= 10;


}
printf("Reversed number is %d\n" , reversednum);
}



