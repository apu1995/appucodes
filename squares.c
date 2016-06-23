#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    long long int a,b,res;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld%lld",&a,&b);
        res=(int)(floor(sqrt(b))-ceil(sqrt(a))+1);
        printf("%lld\n",res);
    }
    return 0;
}

