// another program to see working of sets in c++ 

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main()
{
    int n;
    cin >> n;
    set<int> x, y;
    while(n--)
    {
        int X,Y;
        cin >>X>>Y;
        x.insert(X);
        y.insert(Y);
    }
    if(x.size()==1 || y.size()==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    return 0;
}
