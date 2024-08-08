#include <iostream>
using namespace std;

int main() 
{
    // Users enter three numbers.
    // The program determines whether the triangle is Isoceles,
    // Equilateral or Scalene.

    cout << "Hello, please enter three numbers: ";
    float num1, num2, num3;
    cin >> num1 >> num2 >> num3;

    if (num1 == num2 && num2 == num3) 
    // If there is only one command, you don't need to use the brackets.
        cout << "This forms an equilateral triangle." << endl;
    
    else 
    {
        if (num1 != num2 && num2 != num3) 
            cout << "This is a scalene triangle." << endl;
        
        else
            cout << "This is an isoceles triangle." << endl;   
    }
    return 0;
}