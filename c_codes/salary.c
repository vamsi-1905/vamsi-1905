#include<stdio.h>

#include<math.h>

int main(void)

{

int Monthly_pay , a , b , c

{
    printf("How many hours worked in a week\n");
    scanf("%d" , &a );

    printf("Hourly rate :  ?\n");
    scanf("%d" , &b);

    printf("How many weeks were working in the month\n");
    scanf("%d", &c);

    Monthly_pay = a*b*c;

    printf("Monthly pay is equal to : %d\n", Monthly_pay );
}

}
