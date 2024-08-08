// Lynn T. Aung
// COMP-252
// 2-12-2024
// Assignment 2 - Bank Accounts

#include "BankAccount.h"
#include <iostream>
#include <stdlib.h> 
#include <time.h>

using namespace std;

unsigned int BankAccount::maxAccountID = 0;

BankAccount::BankAccount(string name, unsigned long int phone, string email, 
    double initialDeposit) 
    : accountHolder(name), 
      address(""), 
      email(email), 
      phoneNumber(phone), 
      accountBalance(initialDeposit) {

    maxAccountID++; 
    accountID = maxAccountID; 
}

unsigned int BankAccount::getAccountID() const {
    return accountID;
}

string BankAccount::getAccountHolder() const {
    return accountHolder;
}

string BankAccount::getAddress() const {
    return address;
}

string BankAccount::getEmail() const {
    return email;
}

unsigned long int BankAccount::getPhoneNumber() const {
    return phoneNumber;
}

double BankAccount::getAccountBalance() const {
    return accountBalance;
}

void BankAccount::setAddress(string newAddress) {
    address = newAddress;
}

void BankAccount::setEmail(string newEmail) {
    email = newEmail;
}

void BankAccount::setPhoneNumber(unsigned long int newPhone) {
    phoneNumber = newPhone;
}

void BankAccount::depositMoney(double amount) {
    accountBalance += amount;
    cout << "Successfully deposited $" << amount << " to " << accountHolder <<
    "." << endl;
    cout << "New account balance: $" << accountBalance << "\n" << endl;
}

void BankAccount::printStatement() const {
    cout << "Account Name: " << accountHolder << endl;
    cout << "Account Email: " << email << endl;
    cout << "Account Address: " << address << endl;
    cout << "Account Phone Number: " << phoneNumber << endl;
    cout << "Account Balance: $" << accountBalance << endl;
    cout << "\n" << endl;
}


CheckingAccount::CheckingAccount(string name, unsigned long int phone, 
    string email, double initialDeposit) 
    : BankAccount(name, phone, email, initialDeposit), 
    availableFunds(initialDeposit) {}

double CheckingAccount::getAvailableFunds() const {
    return availableFunds;
}

void CheckingAccount::printStatement() const {
    cout << "Account type: Checking" << endl;
    BankAccount::printStatement();
    cout << "Available Funds: $" << availableFunds << endl;
}

void CheckingAccount::depositMoney(double amount) {
    double deposit = amount * 0.7; 
    availableFunds += deposit;
    BankAccount::depositMoney(amount);
    cout << "Available Funds For " << getAccountHolder() << 
    ": $" << availableFunds << "\n" << endl;
}

bool CheckingAccount::withdrawMoney(double amount) {
    // Check if the available funds is less than or equal to 
    // the account balance and check if the available funds is
    // more than the amount
    if (availableFunds <= accountBalance && availableFunds >= amount) {
        availableFunds -= amount;
        cout << "Withdrawal Successful." << endl;
        cout << "Successfully Withdrew $" << amount << " from " <<
        getAccountHolder() << endl;
        cout << "Available Funds: $" << availableFunds << "\n" << endl;
        return true;
    } else {
        cout << "Withdrawal Unsuccessful. Insufficient Funds." << endl;
        return false;
    }
}

SavingsAccount::SavingsAccount(string name, 
    unsigned long int phone, 
    string email, 
    double initialDeposit) 
    : BankAccount(name, phone, email, initialDeposit), interestRate(0.03) {}

SavingsAccount::SavingsAccount(string name, 
    unsigned long int phone, 
    string email, 
    double initialDeposit, 
    double rate) 
    : BankAccount(name, phone, email, initialDeposit), interestRate(rate) {}

double SavingsAccount::getInterestRate() const {
    return interestRate;
}

void SavingsAccount::setInterestRate(double rate) {
    interestRate = rate;
}

void SavingsAccount::printStatement() const {
    cout << "Account type: Savings" << endl;
    cout << "Account Interest Rate: " << getInterestRate() << endl;
    BankAccount::printStatement();
}

bool SavingsAccount::withdrawMoney(double amount) {
    double penalty = 0.0;
    // Check need to incur penalty
    if (amount > 200) {
        penalty = min(amount * 0.1, 50.0); 
    }
    double totalWithdrawal = amount + penalty;
    // Cannot withdraw more than the account balance
    if (totalWithdrawal < getAccountBalance()) {
        accountBalance -= totalWithdrawal;
        cout << "Withdrawal Successful." << endl;
        cout << "Successfully Withdrew $" << totalWithdrawal << " from " <<
        getAccountHolder() << endl;
        cout << "New Account Balance: " << getAccountBalance() << "\n" << endl;
        return true;
    } else {
        cout << "Withdrawal Unsuccessful. Insufficient Funds." << endl;
        return false;
    }
}

class Bank {
private:
    string bankName;
    BankAccount* accounts[50];
    int numAccounts;

public:
    Bank(string name) : bankName(name), numAccounts(0) {}

    void addAccount(BankAccount* account) {
        // Cannot add more than 50 accounts
        if (numAccounts < 50) {
            accounts[numAccounts] = account;
            numAccounts++;
            cout << "Account Of " << account->getAccountHolder() << 
            " added to the bank: " << bankName << endl;
        } else {
            cout << "Account Add Failed. Full Bank Accounts." << endl;
        }
    }
};

int main() {
    
    srand(time(NULL));

    // Create tester accounts
    CheckingAccount checking1("SCARECROW", 124567890, 
        "scaryscares@example.com", 500.0);

    CheckingAccount checking2("JOKER", 234578901, 
        "jokesRfunny@example.com", 700.0);

    CheckingAccount checking3("BANE", 234678901, 
        "breakbats@example.com", 2000.0);

    SavingsAccount savings1("BATMAN", 345689012, 
        "batman@example.com", 1000.0);

    SavingsAccount savings2("ROBIN", 456780123, 
        "sonofbatman@example.com", 1200.0);

    SavingsAccount savings3("NIGHTWING", 567901234, 
        "richardisaKoolName@example.com", 1500.0);

    // Deposit $1000 in each account
    checking1.depositMoney(1000.0);
    checking2.depositMoney(1000.0);
    checking3.depositMoney(1000.0);
    savings1.depositMoney(1000.0);
    savings2.depositMoney(1000.0);
    savings3.depositMoney(1000.0);

    // Store Bank Pointers
    BankAccount* testAccounts[] = 
        {&checking1, &checking2, &checking3, &savings1, &savings2, &savings3};

    // Deducting Rando Amounts
    for (int i = 0; i < 6; ++i) {
        double randomAmount = rand() % 1001 + 200; 
        testAccounts[i]->withdrawMoney(randomAmount);
    }

    // Print bank statements
    cout << "Printing statements for each account . . ." << endl;
    for (int i = 0; i < 5; ++i) {
        testAccounts[i]->printStatement();
    }

    // Create a Bank
    Bank bank("Wayne Bank");

    // Add at least one account to the Bank
    bank.addAccount(&checking1);
    cout << "\n";

    // Testing setters
    checking1.setAddress("122 Blvd. Las Vegas Texas San Mateo");
    checking1.setEmail("mypast@example.com");
    checking2.setAddress("132 Bla Vlad Road, 120 Exeman");
    checking2.setEmail("NOPEnotmeee@gmail.com");
    savings1.setAddress("BOOHOO ROAD, RAGEFUL Ohio - 123");
    savings1.setEmail("boohoo@gmail.com");
    savings1.setInterestRate(5);
    savings2.setAddress("Bread Crumbs Toast Eggs Sandwich 234");
    savings2.setEmail("scaredycat@yahoo.com");
    savings2.setInterestRate(10);

    checking1.printStatement();
    checking2.printStatement();
    savings1.printStatement();
    savings2.printStatement();


    return 0;
}
