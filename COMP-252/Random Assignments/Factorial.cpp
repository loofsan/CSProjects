#include <iostream>
using namespace std;

// Factorial Recursion

int factorial(int b, int a = 1) {
    if (a == b) {
        return a;
    }
    return a * factorial(b, a+1);
}




int main() 
{
    // Factorial
    cout << "Number: ";
    int num;
    cin >> num;

    cout << "Factorial: " << factorial(num) << endl;


    /*Normal Way

    int factorial = 1;

    for (int i=1;i<=num;i++) {
        factorial *= i;
    }
    

    if (num == 0) {
        cout << "The number is 0." << endl;
    }

    if (num < 0) {
        cout << "Error..." << endl;
    }
    else {
        for (int i=num;i >= 1;i--) {
            factorial *= i;
        }    
        // 16 is the limit as the 'int' can't hold any more digits.
        cout << num << " != " << factorial << endl;
    }

    */

    
    return 0;
}