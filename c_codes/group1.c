#include<stdio.h>
int main(void)
{
    int arr[9] = { 1 , 0 , 0 , 1 , 1, 1, 0 , 0 , 0 };
    int count = 0;
    int temp = 0;
    for(int i =0;i<9;i++)
    {
        if(arr[i]==1){
         count = count +1;}
         else{count = 0;}
       if(temp<count){
       temp = count;}
    }
 printf("%d\n",temp);
}
