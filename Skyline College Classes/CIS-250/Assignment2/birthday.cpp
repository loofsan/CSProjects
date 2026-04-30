/*
    Lynn T. Aung
    CIS - 250
    Assignment 2 - Ages and Birthdays
*/

#include  <iostream>
using namespace std;

int main() {

    // Part I
    int userAge;

    cout << "What is your current age?" << endl;
    cin >> userAge;

    if (userAge < 0) {
        cout << "Ages cannot be negative." << endl;
        return 0;
    }

    int yearsLeftForDecade;
    yearsLeftForDecade = 10 - (userAge % 10);

    // Making sure grammar is correct for different years left
    if (yearsLeftForDecade > 1) {
        cout << "There are " << yearsLeftForDecade << " years left until your next decade birthday." << endl;
    } else {
        cout << "There is " << yearsLeftForDecade << " year left until your next decade birthday." << endl;
    }

    // Part II
    if (userAge <= 17) {
        cout << "Kids birthdays should always be celebrated!" << endl;
    }
    else if (userAge >= 18 && yearsLeftForDecade == 5) {
        cout << "You should throw a party!" << endl;
    }
    else if (userAge >= 18 && yearsLeftForDecade == 1) {
        // In the if statement below, I first get the next decade,
        // then, I divide it by ten to get the integer to check if it is 
        // even or odd since, otherwise, every decade is even.
        if (((userAge + yearsLeftForDecade) / 10) % 2 == 0) { 
            cout << "Plan a HUGE party for your decade birthday!" << endl;
        } else {
            cout << "Plan a big party for your decade birthday!" << endl;
        }
    }
    else if (userAge >= 18) {
        cout << "Have fun with friends and family on your next birthday" << endl;
    }
}