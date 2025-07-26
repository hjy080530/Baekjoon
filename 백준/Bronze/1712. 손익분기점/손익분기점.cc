#include <iostream>
int main() {
    long long a, b, c;
    std::cin >> a >> b >> c;
    if (b>=c) {std::cout << -1;}
    else {std::cout << a/(c-b)+1;}
    return 0;
}