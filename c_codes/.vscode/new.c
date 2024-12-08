#include <stdio.h>

int main(void)
{
    float radius, pi, area;

    printf("Enter radius: ");
    scanf("%f", &radius);

    printf("Enter pi: ");
    scanf("%f", &pi);

    area = radius*radius*pi;

    printf("Area is equal to: %f\n", area);

    return 0;
}



