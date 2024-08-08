#include <iostream>
using namespace std;

int main()
{
    int list[5] = { 2, 3, 5, 7, 9 };

    /*
    cout << list[2] << endl;
    cout << *(list + 2) << endl; // dereferencing array
    */

    for (int i = 0; i <= 4; i++) {
        cout << "Number: ";
        cin >> list[i];
    }

    for (int i = 0; i <= 4; i++) {
        cout << *(list + i) << " ";
    }


    return 0;
}