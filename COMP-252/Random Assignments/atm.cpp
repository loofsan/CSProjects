#include <iostream>
using namespace std;
// Add two users

void showMenu() {
    cout << "**********Menu**********\n" << endl;
    cout << "1. Check Balance" << endl;
    cout << "2. Deposit Money" << endl;
    cout << "3. Withdraw Money" << endl;
    cout << "4. Stop" << endl;
    cout << "************************" << endl;
}

int main() 
{   
    // Check the balance, deposit money, withdraw money, show menu
    int option;
    double balance = 500;    
    
    do {
        showMenu();
        cout << "Choose an option." << endl;
        cin >> option;
        system("cls");
        switch(option) {
        case 1: cout << "Balance is: " << balance << "$" << endl; break;
        case 2: cout << "Deposit amount: ";
            double depositAmount;
            cin >> depositAmount;
            balance += depositAmount; 
            break;
        case 3: cout << "Withdraw: ";
            double withdrawAmount;
            cin >> withdrawAmount;
            if (withdrawAmount <= balance)
                balance -= withdrawAmount;
            else 
                cout << "Not enough money." << endl;
            break;
        }
    } while (option != 4);
    return 0;
}