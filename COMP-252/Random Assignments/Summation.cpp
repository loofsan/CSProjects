#include <iostream>

int main() {
    std::cout << "Enter a range of two numbers: " 
              << std::endl;
    int x = 0, y = 0;
    std::cin >> x >> y;
    int r1 = 0;
    int sum = 0;
    while (x <= y) {
        sum += x;
        ++x;
    }
    std::cout << "The summation of the chosen range ("
              << r1 << "," << y << ") is " << sum << std::endl;

    return 0;
}