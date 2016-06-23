#include <iostream>
#include <limits>
#include <vector>
#include <climits>
#include <cmath>

using namespace std;

int max_left,max_right;

// function to find the maximum subarray across. This can be done in O(n) time.
int max_crossing_subarray(vector <int> a,int low,int mid,int high)
{
	int left_sum=INT_MIN,right_sum=INT_MIN,sum=0;
	for(i=mid;i>=low;i--)
	{
		sum=sum+a[i];
		if(sum>left_sum)
		{
			left_sum=sum;
			max_left=i;
		}
	}
	sum=0;
	for(i=mid+1;i<=high;i++)
	{
		sum=sum+a[i];
		if(sum>right_sum)
		{
			right_sum=sum;
			max_right=i;
		}
	}
	return right_sum+left_sum;
}

// fuction to find out the maximum subarray.

int find_maximum_subarry(vector <int> a, int low , int high)
{
	int left_sum,right_sum,cross_sum,mid;
	if(high==low)
		retun a[low];
	else
	{
		mid=floor((low+high)/2);

		left_sum=find_maximum_subarry(a,low,mid);
		right_sum=find_maximum_subarry(a,mid+1,high);
		cross_sum=max_crossing_subarray(a,low,mid,high);

		if(left_sum>=right_sum && left_sum>=cross_sum)
			return left_sum;
		else if(right_sum>=left_sum && right_sum>=cross_sum)
			return right_sum;
		else
			return cross_sum;
	}
}

int main()
{
	int n,ans;
	cin>>n;
	vector <int> a[n];
	int i;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	ans=find_maximum_subarry(a,0,n-1);
	cout<<ans<<endl;
	return 0;
}