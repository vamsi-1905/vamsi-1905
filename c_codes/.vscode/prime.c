#include <stdio.h>

int main(void) {
    int n, i, isprime = 1;

    printf("Enter n: ");
    scanf("%d", &n);

    if (n <= 1) {
        isprime = 0;
    } else {
        for(i = 2; i < n; i++) {
            if (n % i == 0) {
                isprime = 0;
                break;
            }
        }
    }

    if (isprime)
        printf("It is a prime number.\n");
    else
        printf("It is not a prime number.\n");

    return 0;
}
