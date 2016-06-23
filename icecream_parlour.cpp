// ice cream parlor question solution on hackerrank
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int compareints (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int search(int a[],int n,int x,int s)
{
    int i,pos;
    for(i=s;i<n;i++)
    {
        if(a[i]==x)
        {    
            pos=i;
            break;
        }
    }
    return pos;
}

int main() 
{
    int t,i,n,m,ans,pos,key;
    int * pItem;
    cin>>t;
    while(t--)
    {
        cin>>m;
        cin>>n;
        int a[n],b[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            b[i]=a[i];
        }
        qsort(a,n,sizeof(int),compareints);
        for(i=0;i<n;i++)
        {
            key=m-b[i];
            pItem=(int*)bsearch(&key,a,n,sizeof(int),compareints);
            if(pItem!=NULL)
            {    
                pos=i;
                break;
            }
        }   
        ans=search(b,n,m-b[pos],pos+1);
        cout<<pos+1<<" "<<ans+1<<endl;
    }
    return 0;
}
