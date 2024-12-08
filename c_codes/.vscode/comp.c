#include <stdio.h>
#include <string.h>
int main(void)

{
    int x , y;
    char str0[15] = "good";
    char str1[10] = "google";

     x=strcmp(str0, str1);
    printf("%d",x);
    y = strncmp(str1,str0,3);
    printf("%d",y);
}
