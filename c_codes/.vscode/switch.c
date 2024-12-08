#include<stdio.h>

int main(void)

{
char alphabet;

printf("Enter alphabet: \n");
scanf("%c\n", &alphabet);

switch(alphabet)
{
    case 'a':

    case 'e':

    case 'i':

    case 'o' :

    case 'u' :

    printf("Vowel");
    break;

    default : printf("Consonant");
}
}
