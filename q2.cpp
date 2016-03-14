// Apurva Singh
// Package Problem Solution

#include <iostream>
#include <algorithm>
using namespace std;

int findpos(int temp[],int val,int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(temp[i]==val)
			return i;
	}
}

int main()
{
	int t,n,i,max,sum,k,j,flag;
	float cost[15];
	int weight[15],temp[15],res[15];
	cin>>t; // no of test cases

	while(t--)
	{
		sum=0;
		flag=1;
		cin>>n; //no of elements
		cin>>max; //max weight supported
		for(i=0;i<n;i++)
		{
			cin>>cost[i];
			cin>>weight[i];
			temp[i]=weight[i];
		}
		sort(weight,weight+n);
		sum=weight[0];
		if(sum>max)
			flag=0;
		if(flag)
		{
			for(i=1;i<n;i++)
			{
				if(sum+weight[i]<=max)
				{
					sum=sum+weight[i];
				}
				else
					break;
			}
			k=i;
			for(j=0;j<k;j++)
			{
				res[j]=findpos(temp,weight[j],n);
			}
			sort(res,res+i);
			for(j=0;j<k;j++)
			{
				cout<<res[j]<<" ";
			}
			cout<<"\n";
		}
		else
		{
			cout<<"-\n";
		}
	}
}