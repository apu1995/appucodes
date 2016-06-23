// C program solution to Sherlock and Number problem on Hackerrank.

#include <stdio.h>
int main()
{
	int t,n,c,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		c= ((2*n)%3)*5;
		
		if(c>n)
		{
			printf("-1\n");
		}
		else
		{
			for(i=0;i<n-c;i++)
			{
				printf("5");
			}
			for(i=0;i<c;i++)
			{
				printf("3");
			}
			printf("\n");
		}
	}
	return 0;
}
