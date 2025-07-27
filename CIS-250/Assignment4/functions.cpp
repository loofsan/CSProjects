/*
    Lynn T. Aung
    CIS-250
    Assignment 4 - Functions
    03/04/2025
*/

#include <iostream>
#include <cctype>
using namespace std;

// Function Declarations
bool tripleCheck(int, int, int);
int evenlySpaced(const int [], int);
string capitalize(string);


// Part 1: Triple Check
bool tripleCheck(int num1, int num2, int num3) {

    int largest = 0;
    int small1 = 0;
    int small2 = 0;

    // Find largest one to get c in a^2 + b^2 = c^2
    // since a and b can be interchangeable
    if (num1 > num2 && num1 > num2) {
        largest = num1;
        small1 = num2;
        small2 = num3;
    } else if (num2 > num1 && num2 > num3) {
        largest = num2;
        small1 = num1;
        small2 = num3;
    } else {
        largest = num3;
        small1 = num1;
        small2 = num2;
    }

    int aSqrbSqr = (small1 * small1) + (small2 * small2);
    int cSqr = largest * largest;

    if (aSqrbSqr == cSqr) {
        return true;
    }

    return false;
}

// Part 2: Evenly Spaced
int evenlySpaced(const int list[], int count) {

    // Edge Case
    if (count <= 1) {
        return -1;
    }

    // Get difference between the first two numbers
    int difference = abs(list[1] - list[0]);
    // Check if that difference stays the same
    for(int i = 2; i < count; i++) {
        if (abs(list[i] - list[i - 1]) != difference) {
            return -1;
        } 
    }

    return difference;
}

// Part 3: Capitalize
string capitalize(string s) {

    // Edge Cases
    if (s.empty()) {
        return s;
    }

    s[0] = toupper(s[0]);

    if (s.size() == 1) {
        return s;
    }

    for(int i = 0; i < s.size() - 1; i++) {
        if(s[i] == ' ') {
            s[i + 1] = toupper(s[i + 1]);
        }
    }

    return s;

}


int main() {

    cout << "\nFunctions Testing Program" << endl;
    cout << "================================================" << endl;
    cout << endl;

    cout << "Part 1: Triple Check Tests" << endl;
    cout << "---------------------------" << endl;

    cout << "  Test 1: ";
    cout << (tripleCheck(3, 4, 5) ? "True" : "False") << endl;
    cout << "Expected: True" << endl;

    cout << "  Test 2: ";
    cout << (tripleCheck(10, 3, 1) ? "True" : "False") << endl;
    cout << "Expected: False" << endl;

    cout << "  Test 3: ";
    cout << (tripleCheck(1, 1, 1) ? "True" : "False") << endl;
    cout << "Expected: False" << endl;

    cout << endl;

    cout << "Part 2: Evenly Spaced Tests" << endl;
    cout << "---------------------------" << endl;

    cout << "  Test 1: ";
    const int testArr1[]= {2, 4, 6, 8};
    cout << (evenlySpaced(testArr1, 4)) << endl;
    cout << "Expected: 2" << endl;

    cout << "  Test 2: ";
    const int testArr2[] = {1, 5, 9, 13, 17, 8};
    cout << (evenlySpaced(testArr2, 6)) << endl;
    cout << "Expected: -1" << endl;

    cout << "  Test 3: ";
    const int testArr3[] = {1, 2, 4, 6};
    cout << (evenlySpaced(testArr3, 4)) << endl;
    cout << "Expected: -1" << endl;

    cout << "  Test 4: ";
    const int testArr4[] = {1};
    cout << (evenlySpaced(testArr4, 1)) << endl;
    cout << "Expected: -1" << endl;

    cout << "  Test 5: ";
    const int testArr5[]= {1, 6, 11, 16};
    cout << (evenlySpaced(testArr5, 4)) << endl;
    cout << "Expected: 5" << endl;

    cout << endl;

    cout << "Part 3: Capitalize" << endl;
    cout << "---------------------------" << endl;

    cout << "  Test 1: ";
    string testString1 = "there's no place like home";
    cout << (capitalize(testString1)) << endl;
    cout << "Expected: There's No Place Like Home" << endl;

    cout << "  Test 2: ";
    string testString2 = "Go ahead, make my day.";
    cout << (capitalize(testString2)) << endl;
    cout << "Expected: Go Ahead, Make My Day." << endl;

    cout << "  Test 3: ";
    string testString3 = "Computer";
    cout << (capitalize(testString3)) << endl;
    cout << "Expected: Computer" << endl;
    
    cout << "  Test 4: ";
    string testString4 = "base";
    cout << (capitalize(testString4)) << endl;
    cout << "Expected: Base" << endl;

    cout << "  Test 5: ";
    string testString5 = "      Hello,     this is    with spaces";
    cout << (capitalize(testString5)) << endl;
    cout << "Expected:       Hello,     This Is    With Spaces" << endl;

    cout << endl;

    cout << "================================================" << endl;
    cout << "Testing Finished";

    return 0;
}