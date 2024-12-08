#include<stdio.h>
#include<cs50.h>

int main(void)
{

 int year = get_int("Enter year to check: ");

 if ((year % 4 == 0 && year % 100 != 0 )||(year % 400 == 0))
 {
    printf("It is a leap year\n");
 }
else
{
    printf("It is not a leap year\n");
}
}

