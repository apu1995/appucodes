// project euler problem 2.

#include<stdio.h>
int main()
{
	long long int x1,x2,x3,sum=0;
	x1=1;
	x2=1;
	while(x3<4000000)
	{
		x3=x2+x1;
		x1=x2;
		x2=x3;
		if(x3%2==0)
			sum=sum+x3;
	}
	printf("%lld",sum);
	return 0;
}
