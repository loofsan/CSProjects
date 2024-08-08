#include <iostream>
using namespace std;

int main()
{
    int hostUserNum, guestUserNum;
    cout << "Host: ";
    cin >> hostUserNum;
    system("cls");

    cout << "Guest: ";
    cin >> guestUserNum;

    /*
    if (hostUserNum == guestUserNum) 
        cout << "You guessed it correctly." << endl;
    else
        cout << "You guessed wrong." << endl;
    */

    /* Using Ternary Operator

    (hostUserNum == guestUserNum)? cout << "Correct!": cout << "Failed!";
    */
   
    while (hostUserNum != guestUserNum) {
        cout << "Failed!" <<endl;
        cout << "Guest: ";
        cin >> guestUserNum;
    }
    if (hostUserNum == guestUserNum) {
        cout << "Correct!" << endl;
    }

    return 0;
}