#include<stdio.h>
int main(void)

{   int size;

    printf("What is size?\n");
    scanf("%d" , &size);


   int sequence[size];

    sequence[0] = 1;

    printf("%d\n" , sequence[0]);

    for(int i = 1 ; i < size; i++)
    {
        sequence[i] = sequence[i-1]*2;
        printf("%d\n" , sequence[i]);
    }

}

