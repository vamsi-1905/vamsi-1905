#include<stdio.h>

int search(int arr[],int size ,int x)
   {

   for(int i =0;i<size;i++)
   {
    if(arr[i]==x){
        return i;
        }
   }
   return -1;
   }
int main(void){
    int m,x,sum=0;
    printf("Enter size of array\n");
    scanf("%d",&m);
    int arr[m];
    printf("Enter elements of the array\n");
    for(int i =0;i<m;i++)
    {
    scanf("%d",&arr[i]);
    }
   printf("Enter element to be searched for\n");
   scanf("%d",&x);

  int result = search(arr,m,x);

   if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found in the array\n");
    }
}

