#include <iostream>
using namespace std;

int main()
{
    //Multiplication Table
    cout << "**Multiplication Table**\n" << endl;
    for (int i = 1; i <= 10; i++) {
        for (int a = 1; a <= 10; a++) {
            cout << i << "*" << a << "=" << i*a << endl;
        }
        cout << endl;
    }
    
    return 0;
}