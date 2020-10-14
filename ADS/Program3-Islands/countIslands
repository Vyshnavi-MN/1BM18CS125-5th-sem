#include <bits/stdc++.h> 
using namespace std;
class DisjointSets
{
    int n;
    vector<int> rank;
    vector<int> parent;
    public:
    DisjointSets(int n)
    {
        this->n = n;
        rank.resize(n);
        parent.resize(n);
        for(int i=0;i<n;i++)
            parent[i]=i;
    }
    int find(int x)
    {
        if(x==parent[x]) return x;
        return find(parent[x]);
    }
    void Union(int x,int y)
    {
        int X = find(x);
        int Y = find(y);
        if(X==Y)
                return;
        if(rank[X]==rank[Y])
        {
            parent[Y]=X;
            rank[X]++;
        }
        else if(rank[X]<rank[Y])
        {
            parent[X]=Y;
        }
        else
            parent[Y]=X;
    }
};
int count(vector<vector<int>> &arr)
{
    int n = arr.size();
    int m = arr[0].size();
    DisjointSets *dis = new DisjointSets(n*m);
    for (int j = 0; j < n; j++) 
    { 
        for (int k = 0; k < m; k++) 
        { 
             
            if (arr[j][k] == 0) 
                continue; 
  
            if (j + 1 < n && arr[j + 1][k] == 1) 
                dis->Union(j * (m) + k,  
                          (j + 1) * (m) + k); 
            if (j - 1 >= 0 && arr[j - 1][k] == 1) 
                dis->Union(j * (m) + k,  
                          (j - 1) * (m) + k); 
            if (k + 1 < m && arr[j][k + 1] == 1) 
                dis->Union(j * (m) + k,  
                          (j) * (m) + k + 1); 
            if (k - 1 >= 0 && arr[j][k - 1] == 1) 
                dis->Union(j * (m) + k, 
                          (j) * (m) + k - 1); 
            if (j + 1 < n && k + 1 < m &&  
                    arr[j + 1][k + 1] == 1) 
                dis->Union(j * (m) + k,  
                          (j + 1) * (m) + k + 1); 
            if (j + 1 < n && k - 1 >= 0 &&  
                    arr[j + 1][k - 1] == 1) 
                dis->Union(j * m + k,  
                          (j + 1) * (m) + k - 1); 
            if (j - 1 >= 0 && k + 1 < m &&  
                     arr[j - 1][k + 1] == 1) 
                dis->Union(j * m + k,  
                          (j - 1) * m + k + 1); 
            if (j - 1 >= 0 && k - 1 >= 0 &&  
                     arr[j - 1][k - 1] == 1) 
                dis->Union(j * m + k,  
                          (j - 1) * m + k - 1); 
        } 
    } 
    int *fr = new int[n*m];
    int ans=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(arr[i][j]==1)
            {
                int a = dis->find(i*m+j);
                if(fr[a]==0)
                {
                    ans++;
                    fr[a]++;
                }
                else
                   fr[a]++;
            }
        }
    }
    return ans;
}
int main()
{
    vector<vector<int>>arr = {{1, 1, 0, 0, 0}, 
                            {0, 1, 0, 0, 1}, 
                            {1, 0, 0, 1, 1}, 
                            {0, 0, 0, 0, 0}, 
                            {1, 0, 1, 0, 1}}; 
    cout << "Number of Islands= " 
         << count(arr) << endl; 
}
