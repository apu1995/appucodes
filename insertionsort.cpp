// insertion sort in c++ 

#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
void display(int n, int a[])
{
    int i;
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
void insertionSort(int n, int a[])
{
    int i,j,key;
    for(i=1;i<n;i++)
    {
        key=a[i];
        j=i-1;
        while(j>=0 && a[j]>key)
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
        display(n,a);    
    }
    
}
int main(void) 
{   
    int n;
    cin >>n;
    int a[n],i;
    for(i=0;i<n;i++) 
    { 
       cin>>a[i];
    }
    insertionSort(n,a);
    return 0;
}
