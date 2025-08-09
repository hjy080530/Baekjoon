#include <iostream>
#include <string>

int main() {
    std::string a, b;
    std::cin >> a >> b;

    if (a.size() < b.size())
        a = std::string(b.size() - a.size(), '0') + a;
    else if (b.size() < a.size())
        b = std::string(a.size() - b.size(), '0') + b;

    std::string result;
    result.reserve(a.size() * 2);

    for (size_t i = 0; i < a.size(); ++i) {
        int da = a[i] - '0';
        int db = b[i] - '0';
        result += std::to_string(da + db);
    }

    std::cout << result << "\n";
    return 0;
}