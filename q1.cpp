#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    unsigned int n;
    cin>>t;
    while(t--)
        {
            cin>>n;
            cout<<~n;
        }
    return 0;
}