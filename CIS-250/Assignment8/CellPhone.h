/*
    Lynn T. Aung
    CIS-250
    Assignment 8 - Use Templates
    5/14/2025
*/

#ifndef CELLPHONE_H
#define CELLPHONE_H

#include <string>
#include <iostream>

using namespace std;

class CellPhone {
    protected:
        string model;
        string owner;
        long int phoneNumber; 

    public:
        
        CellPhone(const string& model, const string& owner, long int number);

        CellPhone(const string& owner, long int number);

        virtual void dial() const;

        virtual void hangup() const;

        // Getters 
        string getModel() const;
        string getOwner() const;
        long int getPhoneNumber() const;

        // Setters 
        void setModel(const string& newModel);
        void setOwner(const string& newOwner);
        void setPhoneNumber(long int newNumber);

        // Equality Operator
        bool operator==(const CellPhone &other) const;
};



class FlipPhone : public CellPhone {
    public:
        
        FlipPhone(const string& model, const string& owner, long int number);

        void hangup() const override;

};



class SmartPhone : public CellPhone {
    private:
        string operatingSystem;
        string memorySize; 

    public:
        
        SmartPhone(const string& owner, long int number, const string& os, 
            const string& memory);

        void hangup() const override;

        void dial() const override;
};

#endif 