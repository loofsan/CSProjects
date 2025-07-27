/*
    Lynn T. Aung
    CIS-250
    Assignment 5 - Recursion
    03/23/2025
*/


#include <iostream>
using namespace std;


int maxDigit(int input) {
    
    // Base case: the input is less than 10
    if (input < 10) {
        return input;
    }

    int currentLastDigit = input % 10;
    // The input is reduced by a degree 
    int result = maxDigit(input / 10);

    return (currentLastDigit > result ? currentLastDigit : result);
}

string recurseReverse(const string &input) {

    // If the string is one letter, return
    if (input.size() < 2) {
        return input;
    }

    char lastLetter = input[input.size() - 1];
    // The function recurses on a string without the last character
    // we saved
    string remainingString  = recurseReverse(input.substr(0, input.size()-1));

    return (lastLetter + remainingString);
}


int main() {

    cout << "Testing Recursive Functions" << endl;
    cout << "=================================" << endl;
    cout << endl;

    cout << "Testing Max Digit" << endl;
    cout << "Input: 4562" << endl;
    cout << "Output: " << maxDigit(4562) << endl;
    cout << endl;

    cout << "Testing Reverse String" << endl;
    cout << "Input: rabbit" << endl;
    cout << "Output: " << recurseReverse("rabbit") << endl;
    cout << endl;



    return 0;
}
