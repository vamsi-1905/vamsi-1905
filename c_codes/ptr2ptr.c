#include<stdio.h>
int main(void){
    int a = 10;
    int *ptr = &a;
    int **ptr2ptr = &ptr;


     printf("Value of a: %d\n", a);             
    printf("Value using *ptr: %d\n", *ptr);
    printf("Value using **ptr2ptr: %d\n", **ptr2ptr);

     printf("Address stored in ptr: %p\n", ptr);
     printf("Address of ptr: %p\n", &ptr);
    printf("Address stored in ptr2ptr: %p\n", ptr2ptr);

}
