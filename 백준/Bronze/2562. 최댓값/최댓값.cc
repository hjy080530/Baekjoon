#include <iostream>
using namespace std;

int main() {
    int max = 0;
    int index = 0;
    int num;

    for (int i = 1; i <= 9; ++i) {
        cin >> num;
        if (num > max) {
            max = num;
            index = i;
        }
    }

    cout << max << "\n" << index;
    return 0;
}