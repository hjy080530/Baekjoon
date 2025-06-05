#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> h(N);
    for (int i = 0; i < N; ++i) cin >> h[i];

    int result = 0;

    for (int i = 0; i < N; ++i) {
        int visible = 0;

        for (int j = 0; j < N; ++j) {
            if (i == j) continue;

            bool canSee = true;
            double x1 = i, y1 = h[i];
            double x2 = j, y2 = h[j];

            for (int k = min(i, j) + 1; k < max(i, j); ++k) {
                double x = k;
                double expectedY = y1 + (y2 - y1) * (x - x1) / (x2 - x1);
                if (h[k] >= expectedY) {
                    canSee = false;
                    break;
                }
            }

            if (canSee) visible++;
        }

        result = max(result, visible);
    }

    cout << result << endl;
    return 0;
}