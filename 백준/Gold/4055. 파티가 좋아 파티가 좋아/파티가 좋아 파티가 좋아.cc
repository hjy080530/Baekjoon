#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false), cin.tie(0), cout.tie(0)
using namespace std;

#define X first
#define Y second

bool attend[50];

int main()
{
    fastio;
    for(int t = 1;;t++)
    {
        memset(attend, false, sizeof(attend));
        int p, cnt = 0;
        vector<pair<int, pair<int, int>>> v;
        cin >> p;
        if(p == 0) return 0;
        
        for(int i = 0;i<p;i++)
        {
            int st, en;
            cin >> st >> en;
            if(st == en) continue;
            v.push_back({en - st, {st * 2, en * 2}});
        }   
        
        sort(v.begin(), v.end());

        for(auto e : v)
        {
            for(int i = e.Y.X;i<e.Y.Y;i++)
            {
                if(!attend[i])
                {
                    attend[i] = true;
                    cnt++;
                    break;
                }
            }
        }

        cout << "On day " << t << " Emma can attend as many as " << cnt << " parties.\n";
    }
}