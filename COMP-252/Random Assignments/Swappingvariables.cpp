#include <iostream>
using namespace std;

int main() 
{
    // Program for swapping values of two variables
    // using another temp variable.

    int a = 20;
    int b = 10;

/*
    int temp = a;
    a = b;
    b = temp;

    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
*/

    a = a + b; //30
    b = a - b; //20
    a = a - b; //10

    return 0;
}