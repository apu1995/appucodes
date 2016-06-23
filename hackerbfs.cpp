// shortest path using dfs solution to hackerrank problem.

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
 
int minDistance(int dist[], bool sptSet[],int V)
{
   int min = INT_MAX, min_index;
   for (int v = 0; v < V; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
   return min_index;
}
 
void printSolution(int dist[], int V)
{
   for(int i=0;i<V;i++)
   {
      if(dist[i]==INT_MAX)
          dist[i]=-1;
      if(dist[i])
          cout<<dist[i]<<" ";
   }
   cout<<endl;
}
 
void dijkstra(int graph[1000][1000], int src, int V)
{
    int dist[V];   
	bool sptSet[V]; 
	 
	for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
 
     dist[src] = 0;
 
     for (int count = 0; count < V-1; count++)
     {
       int u = minDistance(dist, sptSet,V);
       sptSet[u] = true;
       
       for (int v = 0; v < V; v++)
         if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u]+graph[u][v] < dist[v])
            	dist[v] = dist[u] + graph[u][v];
     }
     
	 printSolution(dist, V);
}


int main() 
{
    int t,n,m,x,y,s,i,j;
    int e[1000][1000];
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                e[i][j]=0;
        for(i=0;i<m;i++)
        {
            cin>>x>>y;
            e[x-1][y-1]=6;
        }
        cin>>s;
        dijkstra(e,s-1,n);
    }
    return 0;
}
