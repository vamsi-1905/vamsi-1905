#include<stdio.h>
#include<string.h>
int main(void){
    int l1,l2,i,j=0;
    char s1[100]="amrita";
    char s2[100]="blr";
    l1 = strlen(s1);
    l2 = strlen(s2);
    for( i=l1;j<l2;i++,j++)
    {
        s1[i]=s2[j];
    }

s1[i]='\0';
printf("%s\n",s1);

}

