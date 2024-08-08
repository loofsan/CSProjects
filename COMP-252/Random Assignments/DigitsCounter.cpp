#include <iostream>
using namespace std;

int main() 
{
    // Count digits of a number
    cout << "Please enter a number of any digits: ";
    int num;
    cin >> num;

    if (num == 0)
        cout << "You have entered 0." << endl;
    else {
        if (num<0) 
        //  num = abs(num);
            num *= -1;

        int counter = 0;
        // while(num > 0 || num < 0) {}
        while(num > 0) {
            num /= 10;
            counter++;
        }
        cout << "It has " << counter << " digits." << endl;
    }

    return 0;
}