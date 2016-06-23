// hour at 9 solution for problem 1 at Hackerrank.

#include <stdio.h>

int main()
{
	int n,a[1000],i,count;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	count=0;
	for(i=0;i<n-1;i++)
	{
		if(a[i]%2==1)
		{
			a[i]=a[i]+1;
			a[i+1]++;
			count=count+2;
		}
	}
    if(a[n-1]%2==0 && a[n-2]%2==0)
		{
			printf("%d\n",count);
		}
		else
			printf("NO\n");
	return 0;
}
