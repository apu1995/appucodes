// find if the string is pangram ie has all the alphabets.
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <cstring>
using namespace std;


int main() 
{
    set<char> s1;
    int i,len;
    char s[1000];
    cin.getline(s,sizeof(s));
    len=strlen(s);
    for(i=0;i<len;i++)
    {
        if(isalpha(s[i]))
        {
            s1.insert(tolower(s[i]));
        }
    }
    if(s1.size()==26)
        cout<<"pangram"<<endl;
    else
        cout<<"not pangram"<<endl;
    return 0;
}
