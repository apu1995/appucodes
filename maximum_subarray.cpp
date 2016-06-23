// maximum subarry using dynamic programming.
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    long long int t,n,sum,m,i;
    cin>>t;
    while(t--)
    {
        cin>>n;
        sum=0;
        long long int a[n],s[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]>0)
                sum=sum+a[i];
        }
        s[0]=a[0];
        m=s[0];
        for(i=1;i<n;i++)
        {
            s[i]=max(s[i-1]+a[i],a[i]);
            if(s[i]>m)
                m=s[i];
        }
        if(m<0)
            sum=m;
        cout<<m<<" "<<sum<<endl;
    }
    return 0;
}