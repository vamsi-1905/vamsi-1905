#include<stdio.h>

int main(void)
{ int x = 0 , y = 0 , result;

    // Determining the result for switch case
    if (x == y)
        result = 1;
    else if (x > y)
        result = 2;
    else
        result = 3;

    // Using switch to print the appropriate result
    switch (result) {
        case 1:
            printf("1\n"); // x is equal to y
            break;
        case 2:
            printf("2\n"); // x is greater than y
            break;
        case 3:
            printf("3\n"); // x is less than y
            break;
        default:
            printf("Invalid\n");
    }

    return 0;
}

