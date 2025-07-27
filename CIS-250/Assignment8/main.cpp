/*
    Lynn T. Aung
    CIS-250
    Assignment 8 - Use Templates
    5/14/2025
*/


#include "CellPhone.h" 
#include <iostream>
#include <vector>   

using namespace std;

int main() {


    vector<CellPhone*> cellPhones;
    CellPhone* phone1 = new CellPhone("Nokia", "John", 1999111222);
    CellPhone* phone2 = new CellPhone("Samsung", "Doe", 1888222333);
    CellPhone* phone3 = new CellPhone("Google", "Smith", 1999333444);
    CellPhone* phone4 = new CellPhone("Iphone", "Chris", 1999142342);

    cellPhones.push_back(phone1);
    cellPhones.push_back(phone2);
    cellPhones.push_back(phone3);
    cellPhones.push_back(phone4);

    CellPhone phone5("Iphone", "Kevin", 1999142342);

    for (const CellPhone* phonePtr : cellPhones) {
        if (*phonePtr == phone5) { 
            cout << "Phone Matches!" << endl;
            cout << phonePtr->getOwner() << "'s phone is similar to " 
                << phone5.getOwner() << "'s phone." << endl;
        } else {
            cout << "Match not found!" << endl;
        }
    }

    return 0;
}