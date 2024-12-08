#include <stdio.h>

int main() {
	int a0,a1,a2,i,n=0,x,y,z;
	scanf("%d%d%d",&a0,&a1,&a2);
	for(i=0;i<n;i++)
	{
	scanf("%d",&n);
	x = (a0||a1);
    y = (a1||a2);
    z =  (x || y);
	if(z == 1)
	{
	    printf("Not now\n");
	}
	else
	{
	    printf("Water filling time\n");
	}
	}

}
