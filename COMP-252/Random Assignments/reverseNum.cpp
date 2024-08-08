#include <iostream>
using namespace std;

int main() 
{
    // Reversing number

    int number, reversedNumber = 0;
    cout << "Number: ";
    cin >> number;

    while (number != 0) {
        reversedNumber *= 10;
         //int tempNum = number%10; //Taking the last digit of the number
        reversedNumber += number % 10;
        number /= 10;
    }

    cout << "The number reversed is " << reversedNumber << endl;
    
    return 0;
}