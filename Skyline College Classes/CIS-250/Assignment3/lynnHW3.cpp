/*
    Lynn T. Aung
    CIS-250
    Assignment 1 - Array Power
*/
#include <iostream>
using namespace std;

int main() {

    /* Part 1 */
    const int NUM_CAPACITY {30};
    int numbers[NUM_CAPACITY] {0, 1};
    // Fill the array with numbers following the Gub formula
    for(int i = 2; i <= 29; i++) {
        numbers[i] = (i*i) - numbers[i-1];
    }

    /* Part 2 */

    // declare variables for the loop questions
    int userNum;
    string userConfirmation;

    do {
        cout << "Enter an index number between 0 and 29 to find the value at that" << 
            " place in the sequence:" << endl;
        // There is an edge case here that I didn't fix. If the user entered a string 
        // instead of a integer, there would be an error, which I would need to use
        // <limits> to handle it, I think.
        cin >> userNum;

        // Check if the number inputted is valid.
        if (userNum < 0 || userNum > 29) {

            cout << "\nThe number you've entered is out of bounds.\n" << 
                "Please re-enter a valid value. (0 - 29)\n" << endl;

        } else {

            cout << "The value is: " << numbers[userNum] << endl;

        }
        
        do {

            cout << "Would you like to find another value? (y/n): ";
            cin >> userConfirmation;

            // The program would still run fine if the user didn't 
            // use 'n' to stop and used 'ajdcn' but I thought it would
            // feel wrong so I put in this check.

            if (userConfirmation != "y" && userConfirmation != "n") {

                cout << "\nInvalid input. Please enter 'y' for yes" << 
                    " or 'n' for no.\n" << endl;

            }

        } while (userConfirmation != "y" && userConfirmation != "n");
        
    } while (userConfirmation == "y");

    return 0;
}
