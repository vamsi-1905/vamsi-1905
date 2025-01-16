#include<stdio.h>
#include<math.h>
int main(void)
{
    int n , remainder , sum=0 , originalnum;

    printf("Enter the number: ");
    scanf("%d" , &n);

    originalnum = n;

    while(n!=0)
    {
        remainder = n % 10;
        sum += pow(remainder ,3);
        n /= 10;
  }
 if(originalnum == sum)
 {
  printf("It is a amstrong number\n" , originalnum);
  }
  else
  {
    printf("It is not a amstrong number\n" , originalnum);
  }
}

