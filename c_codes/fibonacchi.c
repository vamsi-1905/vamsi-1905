#include<stdio.h>

int main(void)

{
    int a , b , c , i , n=10;
    a = 0 , b = 1;

    printf("%d  , %d" , a,b);

    for(i = 0 ; i<=n ; i++)
    {
      c = a + b;
     printf("%d " , c);
     a = b;
     b = c;
    }
}
