#include<stdio.h>
int main(void)
{
    int rangelow,rangehigh,i,j,isprime=1;

   printf("Enter lower limit: \n");
   scanf("%d" , &rangelow);

   printf("Enter upper limit: \n");
   scanf("%d" , &rangehigh);

    printf("Prime numbers between %d and %d are:\n", rangelow, rangehigh);

    for(i = rangelow; i < rangehigh; i++)
    {

    isprime = 1;

    for(j = 2; j <= i/2; j++)
    {
    if(i%j == 0)
    {
    isprime = 0;
    break;
    }
}

    if(isprime)
    {
        printf("%d " , i);
    }
    }
    printf("/n");
}
