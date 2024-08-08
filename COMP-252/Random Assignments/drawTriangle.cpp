#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int length;
    cout << "Length: ";
    cin >> length;
    char symbol;
    cout << "Enter Symbol: ";
    cin >> symbol;

    for (int i = 1; i <= length; i++) {
        for (int a=1; a <= i;a++) {
            cout << setw(2) << symbol;
        }
        cout << endl;
    }

    cout << "\n" << endl;

    for (int i = length; i >= 1; i--) {
            for (int a = i; a >= 1;a--) {
                cout << setw(2) << symbol;
            }
        cout << endl;
    }
    return 0;
}