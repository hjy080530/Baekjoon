#include <iostream>

using namespace std;
int main() {
    long long x,y,z;
    cin >> x >> y;

    z = y *100/x;
    long long left = 1;
    long long right = 1e9;
    long long answer = -1;

    while (left <= right) {
        long long mid = (left + right) / 2;

        long long real_z = (y + mid) * 100 / (x+ mid);

        if (real_z > z) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << answer;


    return 0;
}