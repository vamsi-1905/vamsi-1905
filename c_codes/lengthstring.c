#include<stdio.h>
int main(void)
{
    char str[10];
    printf("enter string\n");
    scanf("%s",str);
    int l =0;

   for(int i=0;str[i]!='\0';i++)
 {
    l++;
 }
printf("Lenght is %d\n",l);
}
