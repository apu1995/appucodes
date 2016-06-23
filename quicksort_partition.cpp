// the partitioning step in quick sort, the pivot is selected as the first element.

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
void display(vector <int> a)
{
    int i;
    for(i=0;i<a.size();i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
void partition(vector <int> a)
{
   int i,p;
   vector <int> b;
   p=a[0];
   for(i=0;i<a.size();i++)
   {
       if(a[i]<p)
           b.push_back(a[i]);
   }
   b.push_back(p);
   for(i=0;i<a.size();i++)
   {
       if(a[i]>p)
           b.push_back(a[i]);
   }
   display(b);
}
int main(void) 
{
   vector <int> a;
   int n;
   cin >>n;    
   for(int i=0;i<n;i++) 
   {
        int temp;
        cin >>temp;
        a.push_back(temp); 
   }
   partition(a);
   return 0;
}
