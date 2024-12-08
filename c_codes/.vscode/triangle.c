#include<stdio.h>

int main(void)

{
    int AB , BC , AC;

    printf("Enter length of all\n");
    scanf("%d,%d,%d" , &AB, &BC , &AC);

if(AB == BC && BC == AC)
{
    printf("It is equilateral\n");

}
else if(( AB != BC && BC != AC))
{
    printf("It is scalene\n");
}
else
{
    printf("It is isoceles\n");
}
}
