/*
    Lynn T. Aung
    CIS-250
    Assignment 7 - Inheritance
    4/24/2025
*/


#include "CellPhone.h" 
#include <iostream>
#include <vector>   

using namespace std;

int main() {

    CellPhone cell1("Nokia", "John", 1999111222);
    FlipPhone flip1("Samsung", "Doe", 1888222333);
    SmartPhone smart1("Charlie", 1777333444, "Android", "128GB");
    SmartPhone smart2("David", 1666444555, "iOS", "256GB");

    CellPhone* cellptrArr[] = {&cell1, &flip1, &smart1, &smart2};

    for(CellPhone* cellptr : cellptrArr) {
        if (cellptr) {
            cellptr->dial();
            cellptr->hangup();
        }
        cout << endl;
    }

    cout << endl;


    // Testing Getters & Setters
    cout << "==== Testing Getters & Setters ====" << endl;
    
    cout << "Expected: John" << endl;
    cout << "Result: ";
    cout << cell1.getOwner() << endl;

    cout << "Expected: Samsung" << endl;
    cout << "Result: ";
    cout <<  flip1.getModel() << endl;

    cout << "Expected: 1777333444" << endl;
    cout << "Result: ";
    cout << smart1.getPhoneNumber() << endl;

    cout << endl;

    cout << "Setting new variables . . ." << endl;

    cell1.setOwner("Bob");
    flip1.setModel("Pixel");
    smart1.setPhoneNumber(1978324212);

    cout << endl;

    cout << "Expected: Bob" << endl;
    cout << "Result: ";
    cout << cell1.getOwner() << endl;

    cout << "Expected: Pixel" << endl;
    cout << "Result: ";
    cout <<  flip1.getModel() << endl;

    cout << "Expected: 1978324212" << endl;
    cout << "Result: ";
    cout << smart1.getPhoneNumber() << endl;

    cout << "==== End Testing ====" << endl;

    return 0;
}