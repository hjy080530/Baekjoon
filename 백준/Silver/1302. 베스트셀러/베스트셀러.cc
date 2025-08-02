#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, int> books;

    for (int i = 0; i < n; i++) {
        string title;
        cin >> title;
        books[title]++;
    }

    string best;
    int maxCount = 0;
    for (auto& pair : books) {
        if (pair.second > maxCount) {
            maxCount = pair.second;
            best = pair.first;
        }
    }

    cout << best << '\n';
    return 0;
}