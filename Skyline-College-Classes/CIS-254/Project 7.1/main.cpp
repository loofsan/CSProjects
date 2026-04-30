/*
  Lynn T. Aung
  CIS - 254
  Project 7.1
  Find 7
*/

#include <iostream>
using namespace std;

int main() {

    // Initializations
    const int checkNum = 7;
    int first7Index = -1;
    int second7Index = -1;

    int userInput = 0;
    int numInput;

    cout << "How many numbers will be entered? ";
    cin >> userInput;

    // Loop the number of times the user inputted
    // check if the first index hasn't been inputted yet
    // and if it's 7, if it is, put that as first index
    for(int i = 0; i < userInput; i++) {
        cout << "Enter num: ";
        cin >> numInput;

        if (numInput == checkNum && first7Index == -1) {
            first7Index = i;
        }
        // For the last index of 7, it will keep updating 
        // until the last 7
        if (numInput == checkNum) {
            second7Index = i;
        }
    }

    if (first7Index == -1)
        cout << "Sorry, no 7's were entered." << endl;
    else {
        // Print the results. We add one here because, for example,
        // if the index is at 0, we would see it as 1. If the index 
        // was at 4, we would see it as 5.
        cout << "The first 7 was in position " << first7Index + 1 << endl;
        cout << "The last 7 was in position " << second7Index + 1 << endl;
    }

    return 0;
}

