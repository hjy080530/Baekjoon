#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int count = N / 4;

    for (int i = 0; i < count; ++i) {
        cout << "long ";
    }
    cout << "int";
}