//problem statement : Detect if two integers have opposite signs

#include<stdio.h>
int main()
{
	int x,y;


    int test(int x, int y){
    	return((x^y)<0);
    }

	printf("enter two signed integers\n");
	scanf("%d %d",&x,&y);
	printf("%d %d\n",x,y);
	if (test(x,y)==1)
	{
		printf("opposite sign\n");
    }
    else{
    	printf("same sign\n");
    }


}