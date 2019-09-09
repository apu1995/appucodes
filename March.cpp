#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        char points[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>points[i][j];
            }
        }
        
        int collectedPoints[n][n]{};
        int countOfPaths[n][n]{};
        bool negative=true;
        
        for(int i=n-2;i>=0;i--)
        {
            if(negative && points[i][n-1]!='x')
            {
                collectedPoints[i][n-1]=collectedPoints[i+1][n-1]+((int)points[i][n-1]%48);
                countOfPaths[i][n-1]=1;
            }
            else
            {
                collectedPoints[i][n-1]=-1;
                negative=false;
                countOfPaths[i][n-1]=0;
            }
        }
        negative=true;
        for(int j=n-2;j>=0;j--)
        {
            if(negative && points[n-1][j]!='x')
            {
                collectedPoints[n-1][j]=collectedPoints[n-1][j+1]+((int)points[n-1][j]%48);
                countOfPaths[n-1][j]=1;
            }
            else
            {
                collectedPoints[n-1][j]=-1;
                negative=false;
                countOfPaths[n-1][j]=0;
            }
        }
        
        countOfPaths[n-1][n-1]=1;
        
        for(int i=n-2;i>=0;i--)
        {
            for(int j=n-2;j>=0;j--)
            {
                if( points[i][j]!='x')
                {
                    int tempMax=max(collectedPoints[i+1][j+1],max(collectedPoints[i][j+1],collectedPoints[i+1][j]));
                    int currVal=0;
                    if(points[i][j]!='e')
                    {
                        currVal=((int)points[i][j])%48;
                    }
                    if(tempMax!=-1)
                    {
                        collectedPoints[i][j]=tempMax+currVal;
                        int a=collectedPoints[i][j+1];
                        int b=collectedPoints[i+1][j+1];
                        int c=collectedPoints[i+1][j];
       
                        if(a==tempMax)
                            countOfPaths[i][j]=countOfPaths[i][j]+countOfPaths[i][j+1];
                        if(b==tempMax)
                            countOfPaths[i][j]=countOfPaths[i][j]+countOfPaths[i+1][j+1];
                        if(c==tempMax)
                            countOfPaths[i][j]=countOfPaths[i][j]+countOfPaths[i+1][j];
                    }
                    else 
                        collectedPoints[i][j]=-1;
                }
                else
                {
                    collectedPoints[i][j]=-1;
                }
            }
        }
        
        if(collectedPoints[0][0]!=-1)
            cout<<collectedPoints[0][0]<<" "<<countOfPaths[0][0]<<"\n";
        else
            cout<<"0 0\n";
        
    }
    return 0;
}