// has implementation of Quick Sort and Binary search using inbuilt functions.

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

int main() 
{
    int t,i,n,m;
    int * pItem;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int a[n],b[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            b[i]=a[i];
        }
        int key=2;
        qsort(a,n,sizeof(int),compareints);
        pItem=(int*)bsearch(&key,a,n,sizeof(int),compareints);
        if (pItem!=NULL)
             cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
    return 0;
}
