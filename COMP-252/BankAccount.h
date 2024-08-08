#include <iostream>
using namespace std;

#ifndef SKYLINE_BANK_ACCOUNT
#define SKYLINE_BANK_ACCOUNT

class BankAccount{
private:
    static unsigned int maxAccountID;
        // contains the highest existing accountID
        // this is for internal use only so there is no getter

    unsigned int accountID;
        // generated to contain the next highest existing accountID
        // (when a new account is created, maxAccountID increases)

    string accountHolder; // account holder name
    string address; // account holder address
    string email; // account holder email address
    unsigned long int phoneNumber; // account holder phone number
protected:
    double accountBalance; // how much money is in account
public:
    BankAccount(string name, unsigned long int phone, string email, double initialDeposit );
        // name, phone, and email are all saved to associated member fields
        // initialDeposit should be the accountBalance when the new account is created
        // accountID should be generated based on existing maxAccountID
        // when a new account is created, maxAccountID increases

    // Getter Functions
    unsigned int getAccountID() const;
    string getAccountHolder() const; 
    string getAddress() const; 
    string getEmail() const; 
    unsigned long int getPhoneNumber() const;
    double getAccountBalance() const;

    // Setter Functions
    // (Only contact info can be changed with setters)
    void setAddress(string); 
    void setEmail(string); 
    void setPhoneNumber(unsigned long int);

    // changes to accountBalance can only be done 
    // by using depositMoney or withdrawMoney functions
    virtual void depositMoney(double amount);
        //account balance should be increased by the amount parameter
    virtual bool withdrawMoney(double amount) = 0;
        // pure virtual method - implemented in child classes
        // returns true if withdrawal was successful, false otherwise

    virtual void printStatement() const;
        // prints out all Bank account information (member fields)
        // in user-friendly manner for example:
        // Account Balance: $1.23
};

class CheckingAccount : public BankAccount {
private:
    double availableFunds; 
        // how much of the account balance can actually be withdrawn
public:
    CheckingAccount(string name, unsigned long int phone, string email, double initialDeopsit);
        // availableFunds should start the same as initial deposit
        // Hint: remember you have to call a parent constructor!

    
    double getAvailableFunds() const;   

    void printStatement() const;
        // prints that the account type is "Checking" and availableFund amount
        // prints out all Bank account information (member fields)
        // in user-friendly manner for example:
        // Account Balance: $100.23
        // Available Funds: $49.67

    virtual void depositMoney(double amount);
        //account balance should be increased by the amount parameter
        //only 70% of the amount should be added to availableFunds
            /* 
             * [Why is this a requirement? When you deposit a check at a 
             * bank it is common that only some of it becomes available 
             * to you immediately. In the real world you have to wait a 
             * certain amount of time until the full amount is available.]
             */

    virtual bool withdrawMoney(double amount);
        // check if funds are available for withdraw 
        // available funds must stay less than or equal to accountBalance
        // returns true if withdrawal was successful, false otherwise
};

class SavingsAccount : public BankAccount {
private:
    double interestRate; 

public:
    SavingsAccount(string name, unsigned long int phone, string email, double initialDeopsit);
        //if no interest rate is set the default value should be 0.03
    SavingsAccount(string name, unsigned long int phone, string email, double initialDeopsit, double interestRate);


    double getInterestRate() const;  
    void setInterestRate(double);   
 

    void printStatement() const;
        // prints that the account type is "Savings" and interest rate
        // prints out all Bank account information (member fields)
        // in user-friendly manner for example:
        // Account Balance: $100.23

    virtual bool withdrawMoney(double amount);
        /* 
         * A savings account is supposed to be only for 
         * saving. This means sometimes there is a penalty 
         * (fee) for a withdrawal.
         */
        // There is no penalty for an amount under 200
        // If the withdrawal amount is over $200, 
        // then the penalty is 10% of the amount being withdrawn.
        // No matter how much is withdrawn, 
        // the maximum withdrawal penalty is $50.  
        // The amount withdrawn added to the penalty must be less than the account balance  
        // returns true if withdrawal was successful, false otherwise
            // (if successful account balance should be lower!)
};

#endif

