#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        int c = 0, ans = 0;
        for (char ch : s) {
            if (ch == 'O') { c++; ans += c; }
            else c = 0;
        }
        cout << ans << '\n';
    }
    return 0;
}