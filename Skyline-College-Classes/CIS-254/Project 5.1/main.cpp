/*
  Lynn T. Aung
  CIS - 254
  Project 5.1
  Simple Loop
*/



#include <iostream>
using namespace std;

int main() {

    char userChar;
    int pounds;

    // Get user input
    cout << "Is there a pounds to convert (Y or N)? ";
    cin >> userChar;

    while (userChar == 'Y') {  // Check if the user wants to continue
        cout << "enter pounds: ";
        cin >> pounds;

        int ounces = pounds * 16;  // Convert pounds to ounces
        cout << pounds << " pounds is " << ounces << " ounces." << endl;

        cout << "Is there another pounds to convert? ";
        cin >> userChar;
    }


    return 0;
}