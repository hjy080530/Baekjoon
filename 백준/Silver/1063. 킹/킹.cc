#include <iostream>
#include <string>
#include <map>
using namespace std;

pair<int, int> move(string cmd) {
    map<string, pair<int, int>> dir = {
        {"R", {1, 0}}, {"L", {-1, 0}}, {"B", {0, -1}}, {"T", {0, 1}},
        {"RT", {1, 1}}, {"LT", {-1, 1}}, {"RB", {1, -1}}, {"LB", {-1, -1}}
    };
    return dir[cmd];
}

int main() {
    string king, stone;
    int n;
    cin >> king >> stone >> n;

    int kx = king[0] - 'A';
    int ky = king[1] - '1';
    int sx = stone[0] - 'A';
    int sy = stone[1] - '1';

    while (n--) {
        string cmd;
        cin >> cmd;
        auto [dx, dy] = move(cmd);
        int nkx = kx + dx;
        int nky = ky + dy;

        if (nkx < 0 || nkx >= 8 || nky < 0 || nky >= 8) continue;

        if (nkx == sx && nky == sy) {
            int nsx = sx + dx;
            int nsy = sy + dy;
            if (nsx < 0 || nsx >= 8 || nsy < 0 || nsy >= 8) continue;
            sx = nsx;
            sy = nsy;
        }

        kx = nkx;
        ky = nky;
    }

    cout << char(kx + 'A') << ky + 1 << '\n';
    cout << char(sx + 'A') << sy + 1 << '\n';

    return 0;
}