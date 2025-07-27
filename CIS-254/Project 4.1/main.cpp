/*
  Lynn T. Aung
  CIS - 254
  Project 4.1
  Area Of A Square & Triangle
*/


#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Declaring variables
    char figureType;
    double area;

    // Get user's input on whether they want the area of square 
    // or triangle
    cout << "Enter the type of figure (s or t): ";
    cin >> figureType;

    // if they chose triangle
    if (figureType == 't') {
        double base, height;

        cout << "Enter the base: ";
        cin >> base;
        cout << "Enter the height: ";
        cin >> height;
        // Calculate Area
        area = 0.5 * base * height;
    }
    // Otherwise
    else if (figureType == 's') {
        double side;
        cout << "Enter the length of a side: ";
        cin >> side;
        // Calculate the area for a square
        area = side * side;
    }
    // Print with precision
    cout << fixed << setprecision(1) << "The area is " << area << endl;

    return 0;
}