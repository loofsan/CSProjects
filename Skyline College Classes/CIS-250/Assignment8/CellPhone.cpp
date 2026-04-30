/*
    Lynn T. Aung
    CIS-250
    Assignment 8 - Use Templates
    5/14/2025
*/

#include "CellPhone.h" 
#include <iostream>

using namespace std;

// Implementation Of The Parent Class - CellPhone
// ==============================================

CellPhone::CellPhone(const string& model, const string& owner, long int number)
    : model(model), owner(owner), phoneNumber(number) {}

CellPhone::CellPhone(const string& owner, long int number)
    : CellPhone("Unknown Model", owner, number) {}

void CellPhone::dial() const {
    cout << owner << " is calling from " << phoneNumber << endl;
}

void CellPhone::hangup() const {
    cout << "hanging up cell phone" << endl;
}

string CellPhone::getModel() const {
    return model;
}

string CellPhone::getOwner() const {
    return owner;
}

long int CellPhone::getPhoneNumber() const {
    return phoneNumber;
}

void CellPhone::setModel(const std::string& model) {
    this->model = model;
}

void CellPhone::setOwner(const std::string& owner) {
    this->owner = owner;
}

void CellPhone::setPhoneNumber(long int number) {
    phoneNumber = number;
}

bool CellPhone::operator==(const CellPhone &other) const {
    if (model == other.model && 
        phoneNumber == other.phoneNumber) {
            return true;
    } 
    return false;
}


// Implementation Of The Child Class - FlipPhone
// ==============================================

FlipPhone::FlipPhone(const string& model, const string& owner, long int number)
    : CellPhone(model, owner, number) {}

void FlipPhone::hangup() const {
    cout << "close phone" << endl;
}

// Implementation Of The Child Class - SmartPhone
// ==============================================

SmartPhone::SmartPhone(const string& owner, long int number, const string& os, 
    const string& memory)
    : CellPhone(owner, number), operatingSystem(os), memorySize(memory) {}

void SmartPhone::hangup() const {
    cout << "press end button" << endl;
}

void SmartPhone::dial() const {
    cout << model << " with " << operatingSystem << " is calling from " 
    << phoneNumber << endl;
}