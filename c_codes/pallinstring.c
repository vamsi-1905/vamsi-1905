#include<stdio.h>
#include<string.h>
int main(void){

    char string[100];int count=0;
    printf("Enter string to be checked");
    scanf("%99s",string);

    int j = strlen(string)-1;

    for(int i = 0; i < j;i++)
    {
    if(string[i]==string[j])
    {
        
        j--;
    if(i>=j)
    {
        count = 2;
        break;
    }
    }
    else{
    count = 1;
    break;
    }
    }
    if(count == 1){
    printf("It is not a pallindrome");}
    else
    {
    printf("It is a pallindrome");
    }
}


