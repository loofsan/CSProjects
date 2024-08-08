// Lynn T. Aung 
// Assignment 1 - Circle Program
// 1-22-24

#include <iostream>
using namespace std;

int main() {

    const float PI = 3.1416;
    float radius;

    cout << "Please enter the radius of the circle: ";
    cin >> radius;

    float area = PI * radius * radius;
    cout << "The area is " << area;

    return 0;

}