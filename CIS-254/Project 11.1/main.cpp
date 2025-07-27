/*
  Lynn T. Aung
  CIS - 254
  Project 11.1
*/



#include <iostream>
#include <iomanip>
#include <string>

using namespace std;


const int MONTHS_IN_YEAR = 12;







// Function to determine if a year is a leap year
bool isLeapYear(int year) {
    if (year % 400 == 0) {
        return true;
    }
    if (year % 100 == 0) {
        return false;
    }
    if (year % 4 == 0) {
        return true;
    }
    return false;
}







// Helper Function to get the number of days in a month
int getDaysInMonth(int month, int year) {
    switch (month) {
        case 2: // February
            if (isLeapYear(year)) {
                return 29;
            }
            else {
                return 28;
            }
        case 4: // April
        case 6: // June
        case 9: // September
        case 11: // November
            return 30;
        default:
            return 31;
    }
}







// Helper Function to get the name of a month
string getMonthName(int month) {
    switch (month) {
        case 1: return "January";
        case 2: return "February";
        case 3: return "March";
        case 4: return "April";
        case 5: return "May";
        case 6: return "June";
        case 7: return "July";
        case 8: return "August";
        case 9: return "September";
        case 10: return "October";
        case 11: return "November";
        case 12: return "December";
        default: return "";
    }
}







// Helper Function to print the month header
void printMonthHeader(string monthName) {
    cout << setw(13) << monthName << endl << endl;
    cout << "  S  M  T  W  T  F  S" << endl;
    cout << "---------------------" << endl;
}







// Function to print the entire month
void printMonth(int year, int month, int startDay) {

    printMonthHeader(getMonthName(month));
    
    for (int i = 0; i < startDay * 3; i++) {
        cout << " ";
    }

    cout << " ";
    
    // Print all days in a single line
    int daysInMonth = getDaysInMonth(month, year);
    for (int day = 1; day <= daysInMonth; day++) {
        cout << setw(2) << day;
        // Only add space if it's not the last day
        if (day < daysInMonth) {
            cout << " ";
        }
    }
    

    cout << endl << endl;
}





int main() {
    int year, startDay;
    
    // Get user input
    cout << "What year do you want a calendar for? ";
    cin >> year;
    
    cout << "What day of the week does January 1 fall on?" << endl;
    cout << "(Enter 0 for Sunday, 1 for Monday, 6 for Saturday, etc.): ";
    cin >> startDay;
    
    // Print the year
    cout << setw(11) << year << endl << endl;
    
    // Print all months
    for (int month = 1; month <= MONTHS_IN_YEAR; month++) {
        printMonth(year, month, startDay);
    }
    
    return 0;
}