#include <stdio.h>
#include <string.h>
int main(void)
{
    char str0[15] = "Amrita";
    char str1[10] = "blr";

    strncat(str0, str1, 2);
    printf("%s\n", str0);

    return 0;
}

