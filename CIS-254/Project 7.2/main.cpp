/*
  Lynn T. Aung
  CIS - 254
  Project 7.2
  Sum Of Squares
*/

#include <iostream>
using namespace std;


int main() {

    int userInput;
    int finalSum;


    // Use do while loop because we're asking this
    // question at least once.
    do {
        cout << "Enter an integer larger than 0 (0 or less to quit): ";
        cin >> userInput;

        if (userInput > 0) {
            finalSum = (userInput * (userInput + 1) * (2 * userInput + 1)) / 6;
            cout << "The sum of the squares from 1 to " << userInput << " is " << finalSum << endl;
        }

    } while (userInput > 0);


    return 0;
}
