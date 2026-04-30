/*
  Lynn T. Aung
  CIS - 254
  Project 4.2
  Education Level Output
*/


#include <iostream>
using namespace std;

int main() {
    // Make constants to calculate the education level
    const int NO_SCHOOL = 0;
    const int ELEMENTARY_SCHOOL_END = 6;
    const int MIDDLE_SCHOOL_END = 8;
    const int HIGH_SCHOOL_END = 12;
    const int MIN_YEARS = 0;

    int yearsOfSchool;

    // Get the number of schools of the user
    cout << "Enter number of years of school: ";
    cin >> yearsOfSchool;

    // Check for edge case
    if (yearsOfSchool < MIN_YEARS) {
        cout << "years of school must be a non-negative integer" << endl;
    }
    else if (yearsOfSchool == NO_SCHOOL) {
        cout << "no school" << endl;
    }
    else if (yearsOfSchool <= ELEMENTARY_SCHOOL_END) {
        cout << "elementary school" << endl;
    }
    else if (yearsOfSchool <= MIDDLE_SCHOOL_END) {
        cout << "middle school" << endl;
    }
    else if (yearsOfSchool <= HIGH_SCHOOL_END) {
        cout << "high school" << endl;
    }
    else {
        cout << "college" << endl;
    }

    return 0;
}
