#include <stdio.h>

int main()
{
	long long int a[10000],diff[10000],x;
	int n,t,i,j,count;
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		scanf("%d",&n);
		scanf("%lld",&a[0]);
		diff[0]=a[0];
		for(i=1;i<n;i++)
		{
			scanf("%lld",&a[i]);
			diff[i]=a[i]-a[i-1];
		}
		for(i=0;i<n;i++)
		{
			scanf("%lld",&x);
			if(x<=diff[i])
			{
				count++;
			}
		}
		printf("%d\n",count);
	}
}