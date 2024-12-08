#include <stdio.h>


int main() {

	int  i, n, a,b,c,counter;
    printf("What is n\t");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("What is a and b");
        scanf("%d%d", &a,&b);
       c = a - b;
       if(c <= 0){
           printf("0\n");
       }
       else {
    counter = 0;
    while(b < a)
    {
        b = b+4;
        counter++;
    }

          printf("%d\n",counter) ;
       }
             }
    }

