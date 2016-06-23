// code to see how to iterate in sets.

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int main() 
{
    int t,n,a,b,i,j;
    cin>>t;
    while(t--)
    {
        cin>>n>>a>>b;
        set<int> s;
        set<int>::iterator it;
        if(a>=b)
        {    
            for(i=0,j=n-1;i<=n-1;i++,j--)
            {
                s.insert(a*i+b*j);
            }
        }
        else if(a<b)
        {
            for(i=0,j=n-1;i<=n-1;i++,j--)
            {
                s.insert(b*i+a*j);
            }
        }
        for (it=s.begin(); it!=s.end(); ++it)
        {
            cout<<*it<<" ";
        }
        cout<<endl;
    }
    
    return 0;
}