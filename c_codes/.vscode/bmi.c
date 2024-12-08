#include<stdio.h>

int main(void)

{
    float h , w , y, bmi;


    printf("What is your height\n");
    scanf("%f" , &h);
    y = 0.30 * h;

    printf("What is your weight\n");
    scanf("%f" , &w);

    bmi = w / (y * y);

    if (bmi <= 18.5)
    {
    printf("Underweight\n");
    }

   else if (18.5 < bmi && bmi <= 24.5)
   {
   printf("Normal Weight\n");
   }

   else
   {
   printf("Over Weight\n");
   }
   return 0;
}


