/*
  Lynn T. Aung
  CIS - 254
  Project 4.3
  Simple Calculator
*/


#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double num1, num2;
    char operation;
    // Get user's inputs on their numbers and the operations they want to do
    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter an operator (+, -, *, or /): ";
    cin >> operation;

    cout << "Enter second number: ";
    cin >> num2;

    double result;
    // Use switch case on the operations and their functions.
    // Could have used if-else too.
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                cout << "Error! Division by zero." << endl;
                return 1;  
            }
            break;
        default:
            cout << "Invalid operator!" << endl;
            return 1; 
    }
    // Print with precision
    cout << fixed << setprecision(2) << "The answer is " << result << endl;

    return 0;
}
