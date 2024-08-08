#include <iostream>
using namespace std;

int main() 
{
    int n = 5;
    cout << &n << endl;

    // Stores the address of n in 'ptr'.
    int *ptr = &n;
    cout << ptr << endl;

    // Dereferences the pointer to get the value of the address
    cout << *ptr << endl;

    // Changes the value that the address holds.
    *ptr = 10;
    cout << *ptr << endl;
    cout << n << endl;

    // Pointer has to be the same type as its variable.

    return 0;
}