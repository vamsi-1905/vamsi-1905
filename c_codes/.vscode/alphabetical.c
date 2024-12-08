#include<stdio.h>
#include<string.h>

int main(void)
{
    char length[100];
    int width;

    printf("Enter a phrase\n");
    scanf("%s", length);

     width = strlen(length);
    for(int i = 0; i < width;i++)

    {
      printf("%i " , length[i]);
    }
     printf("\n");
    return 0;
}
