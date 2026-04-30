/*
    Lynn T. Aung
    CIS-250
    Assignment 6 - Fidget Toy Class
    03/25/2025
*/

#include <iostream>
using namespace std;

class FidgetToy {
    private:
        string name;
        string description;
        int minAge;
        bool isSpinner;
    public:
        FidgetToy(string name, string description, 
            int minAge, bool isSpinner) 
        {
            this->name = name;
            this->description = description;
            this->minAge = minAge;
            this->isSpinner = isSpinner;
        }
        FidgetToy(string name, int minAge)
            : name(name), description(name), 
            minAge(minAge), isSpinner(false) {}

        string getName() const;
        void setName(string name);

        string getDescription() const;
        void setDescription(string description);

        int getMinAge() const;
        void setMinAge(int minAge);

        bool getIsSpinner() const;
        void setIsSpinner(bool isSpinner);

        void describe() const;

        void appendToDescription(string);
};

string FidgetToy::getName() const {
    return name;
}

void FidgetToy::setName(string name) {
    if (name.size() < 3) {
        cout << "Invalid name setting" << endl;
    } else {
        this->name = name;   
    }
}

string FidgetToy::getDescription() const {
    return description;
}

void FidgetToy::setDescription(string description) {
    if (description.size() < 3) {
        cout << "Invalid description setting" << endl;
    } else {
        this->description = description;
    }
    
}

int FidgetToy::getMinAge() const {
    return minAge;
}

void FidgetToy::setMinAge(int minAge) {
    if (minAge < 0) {
        cout << "Invalid minimum age setting" << endl;
    } else {
        this->minAge = minAge;
    }
}

bool FidgetToy::getIsSpinner() const {
    return isSpinner;
}

void FidgetToy::setIsSpinner(bool isSpinner) {
    this->isSpinner = isSpinner;
}

void FidgetToy::describe() const {
    cout << "==== Fidget Toy ====" << endl;
    cout << endl;

    cout << "Name: " << name << endl;
    cout << "Description: " << description << endl;
    cout << "Minimum Age: " << minAge << endl;
    cout << "Is a Spinner: " << 
    (isSpinner ? "Yes" : "No") << endl;

    cout << endl;
    cout << "====================" << endl;
    cout <<  endl;
}

void FidgetToy::appendToDescription(string moreDescription) {

    description += moreDescription;

}


int main() {

    FidgetToy testToy1("Flash", "Very Cool", 3, true);
    FidgetToy testToy2("Superman", 4);
    FidgetToy testToy3("Batman", 10);

    FidgetToy *testToy3ptr = &testToy3;

    testToy3ptr->setMinAge(20);
    testToy3ptr->appendToDescription("is awesome!!");

    FidgetToy fidgetToyArray[3] = {testToy1, testToy2, testToy3};

    for (const FidgetToy& fidgetToy : fidgetToyArray) {
        fidgetToy.describe();
    }
 
    return 0;
}