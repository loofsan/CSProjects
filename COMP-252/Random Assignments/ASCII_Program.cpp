#include <iostream>
using namespace std;

// Ask a user to enter letters and change them to ASCII

// Doesn't consider 'Enters' and 'Backspaces' in the program


int main() // Change letters into ASCII 
{
    char c1, c2, c3, c4, c5;
    cout << "Enter 5 letters : ";
    cin >> c1 >> c2 >> c3 >> c4 >> c5;
    cout << "ASCII message: " << int(c1) << " " << int(c2)
         << " " << int(c3) << " " << int(c4) << " " << int(c5); 

    return 0;

}

int ASCII_to_Letters()
{
    int i1, i2, i3, i4, i5;
    cout << "Enter 5 integers: ";
    cin >> i1 >> i2 >> i3 >> i4 >> i5;
    cout << "Here is your word: " << char(i1) << char(i2)
         << char(i3) << char(i4) << char(i5);

    return 0;
}