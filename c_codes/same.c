#include<stdio.h>
int main(void){
    int i;
    char s1[100]="hello";
    char s2[100]="hola";
    for( i=0;s2[i]!='\0';i++)
    {
        s1[i]=s2[i];
    }

s1[i]='\0';
printf("%s\n",s1);

}

