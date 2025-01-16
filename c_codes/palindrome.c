#include <stdio.h>

int main(void) {
    int n, originalnum, reversednum = 0, remainder;

    printf("Enter value: \n");
    scanf("%d", &n);

    originalnum = n;

    while(n != 0) {
        remainder = n % 10;
        reversednum = reversednum * 10 + remainder;
        n /= 10;
    }

    if(originalnum == reversednum)
        printf("It is a palindrome\n");
    else
        printf("Not a palindrome\n");

}
