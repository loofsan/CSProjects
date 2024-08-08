#include <iostream>
using namespace std;

bool isPrimeNumber(int number) {
    for (int i = 2; i < number; i++) {
        if(number%i == 0) 
            return false;
    }
    return true;
}

int main() 
{
    
    /*int number;
    cout << "Number: ";
    cin >> number;
    
    bool isPrimeFlag = isPrimeNumber(number);

    if (isPrimeFlag) {
        cout << "Prime Number" << endl;
    }
    else
        cout << "Not prime number" << endl;

    */
    int counter = 0;
    int num;
    cout << "Number: ";
    cin >> num;

    for (int i = 1; i <= num; i++) {
        bool isPrime = isPrimeNumber(i);
        if(isPrime) {
            counter++;
        }
    }
    cout << "There are " << counter << " prime numbers between 1 and " 
         << num << endl;
    return 0;
}