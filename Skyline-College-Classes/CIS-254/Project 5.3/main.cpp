/*
  Lynn T. Aung
  CIS - 254
  Project 5.3
  Theater Loop
*/

#include <iostream>
#include <iomanip>
using namespace std;

// Constants for age groups
const int AGE_18 = 18;
const int AGE_30 = 30;
const int AGE_40 = 40;
const int AGE_60 = 60;

int main() {
    
    int age;
    char foodPref;
    
    // Age groups
    int teen = 0, youngAdult = 0, adult = 0, oldAdult = 0, oldOld = 0;

    // Food preferences
    int count_popcorn = 0, count_soda = 0, count_both = 0;

    int totalAge = 0, numAttendees = 0;
    int youngest, oldest = -1;

    // Get age
    cout << "Enter age of attendee (negative number to quit): ";
    cin >> age;
    youngest = age;
    while (age >= 0) {
        // Increment age groups after checking 
        if (age <= AGE_18) {
            teen++;
        } else if (age <= AGE_30) {
            youngAdult++;
        } else if (age <= AGE_40) {
            adult++;
        } else if (age <= AGE_60) {
            oldAdult++;
        } else {
            oldOld++;
        }

        numAttendees++;
        totalAge += age;
        if (age < youngest) youngest = age;
        if (age > oldest) oldest = age;

        // Get Food Pref
        cout << "Enter food preference ('p' for popcorn, 's' for soda, 'b' for both): ";
        cin >> foodPref;

        // Increment food pref
        if (foodPref == 'p') {
            count_popcorn++;
        } else if (foodPref == 's') {
            count_soda++;
        } else if (foodPref == 'b') {
            count_both++;
        }

        // Get input again
        cout << "Enter age of attendee (negative number to quit): ";
        cin >> age;
    }

    // Print 
    if (numAttendees == 0) {
        cout << "\nNo attendees were entered." << endl;
    } else {
        cout << "\nage  0 to 18: " << teen << endl;
        cout << "age 19 to 30: " << youngAdult << endl;
        cout << "age 31 to 40: " << adult << endl;
        cout << "age 41 to 60: " << oldAdult << endl;
        cout << "over 60: " << oldOld << endl;
        cout << endl;
        cout << "food preference popcorn: " << count_popcorn << endl;
        cout << "food preference soda: " << count_soda << endl;
        cout << "food preference both: " << count_both << endl;

        // Change type for decimals
        double averageAge = static_cast<double>(totalAge) / numAttendees;

        cout << fixed << setprecision(1);
        cout << "\nThe average age was " << averageAge << endl;
        cout << "The youngest person in attendance was " << youngest << endl;
        cout << "The oldest person in attendance was " << oldest << endl;
    }

    return 0;
}
