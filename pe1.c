// project euler problem 1

#include<stdio.h>

int main()
{
	int count=0,i;
	for(i=1;i<1000;i++)
	{
		if(i%3==0 || i%5==0)
			count=count+i;
	}
	printf("%d",count);
	return 0;
}

