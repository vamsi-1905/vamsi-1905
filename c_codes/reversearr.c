#include<stdio.h>
int main(void){
    int m,sum=0;
    printf("Enter size of array\n");
    scanf("%d",&m);
    int arr[m];
    printf("Enter elements of the array\n");
    for(int i =0;i<m;i++)
    {
    scanf("%d",&arr[i]);
    printf("%d\n",arr[i]);
    }
    printf("\nArray in reverse order:\n");
    for(int i = m-1; i>=0;i--){
    printf( "%d\n",arr[i]);

}
}
