#include<bits/stdc++.h>
using namespace std;
string secMostRepeated(vector<string> seq)
{
    unordered_map<string, int> occ;
    int first_max = INT_MIN, sec_max = INT_MIN;
    
    for (int i = 0; i < seq.size(); i++) {
        int hash = 0;
        for (int j =0; j < seq[i].size(); j++) {
            hash += (int)(seq[i][j]);
        }
        occ[seq[i]] = occ[seq[i]] + hash;
    }
    
    for (auto it = occ.begin(); it != occ.end(); it++) {
        if (it->second > first_max) {
            sec_max = first_max;
            first_max = it->second;
        }

        else if (it->second > sec_max &&
                 it->second != first_max)
            sec_max = it->second;
    }

    for (auto it = occ.begin(); it != occ.end(); it++) {
        if (it->second == sec_max)
            return it->first;
    }
}

int main()
{
    int n;
    cout<<"Enter number of strings: ";
    cin>>n;
    unordered_map<string,int>map;
    vector<string>arr(n);
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    for(int i=0;i<n;i++)
    {
        map[arr[i]]++;
    }

    string sec_maxe;
    sec_maxe = secMostRepeated(arr);
    cout<<"Element with second highest frequency :"<<sec_maxe<<endl;
    return 1;
}