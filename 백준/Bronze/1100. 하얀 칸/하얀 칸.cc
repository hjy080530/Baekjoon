#include <iostream>
using namespace std;

int main() {
    char board[8][8];
    int count = 0;

    for (int i = 0; i < 8; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < 8; ++j) {
            if ((i + j) % 2 == 0 && row[j] == 'F') {
                count++;
            }
        }
    }

    cout << count << endl;
    return 0;
}