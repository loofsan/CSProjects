/*
    Lynn T. Aung
    CIS-250
    Assignment 5 - Recursion
    03/21/2025
*/

#include <iostream>
using namespace std;

int returnValue(int index) {

    if (index == 0) {
        return 0;
    } 
    if (index == 1) {
        return 1;
    }

    return  (index * index - returnValue(index - 1));
}

int main() {

    for (int i = 0; i <= 10; i++) {
        cout << "n = " << i << ": " << returnValue(i) << endl;
    }

    return 0;
}