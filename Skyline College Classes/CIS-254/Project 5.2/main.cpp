/*
  Lynn T. Aung
  CIS - 254
  Project 5.2
  Another Simple Loop
*/



#include <iostream>
using namespace std;

int main() {

    int userInt;

    // Get user input
    cout << "enter pounds (negative number to quit): ";
    cin >> userInt;

    while (userInt >= 0) {  // Check if the user wants to continue

        int ounces = userInt * 16;  // Convert pounds to ounces
        cout << userInt << " pounds is " << ounces << " ounces." << endl;

        cout << "enter pounds (negative number to quit): ";
        cin >> userInt;
    }


    return 0;
}