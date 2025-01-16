#include <stdio.h>
#include <string.h>
int main(void)

{
    int x , y;
    char str0[15] = "amrita";
    char str1[10] = "tlr";

     x=strcmp(str0, str1);
    printf("%d",x);
    y = strcmp(str1,str0);
    printf("%d",y);
}
