#include<stdio.h>
int main(void){
    int n,sum=0;
    printf("Enter size of array");
    scanf("%d",&n);
    int arr[n];
    printf("Enter elements of the array\n");
    for(int i =0;i<n;i++)
    {
    scanf("%d",&arr[i]);
    if(arr[i]/2!=0)
    sum = sum + i;
    }
    printf("%d",sum);

}