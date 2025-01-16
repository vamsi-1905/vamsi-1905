#include<stdio.h>
int main(void){
    int i=0;
    char s1[100]="amrita";
    char s2[100]="aprita";
    while(s1[i]==s2[1]&&s1[i]!='\0'&&s2[i]!='\0')
    {
        i++;
    }
if (s1[i]=='\0'&& s2[i]=='\0')
printf("Equal");
else
printf("Not equal");

}
