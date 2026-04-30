/*
  Lynn T. Aung
  CIS - 254
  4/14/2025
  Professor Dave Harden
  Project 12.1
  
  This program will print a calendar for a given year, given the day 
  of the week that January 1 falls on. It displays each month with 
  proper formatting with the correct number of days and days of the 
  week. The program handles leap years and maintains the day of the 
  week continuity between months.
  
  Input: Year and the day of the week January 1 falls on 
  (0-6, where 0 is Sunday)

  Output: A formatted calendar for the entire year with each month 
  displayed separately
*/

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const int MONTHS_IN_YEAR = 12;


// Checks if the input year is a leap year
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







// Returns the number of days in the specified 
// month of the given year
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
        default: // Rest of the month
            return 31;
    }
}








// Returns the name of the specified month
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








// Prints the header for a month, including its name and
// days of the week
void printMonthHeader(string monthName) {
    cout << setw(13) << monthName << endl << endl;
    cout << "  S  M  T  W  T  F  S" << endl;
    cout << "---------------------" << endl;
}







// Prints the calendar for a specified month of a given year, 
// starting on startDay. Updates startDay to be the starting
// day for the next month
void printMonth(int year, int month, int& startDay) {
    printMonthHeader(getMonthName(month));
    
    int currentDay = startDay;
    
    // Print leading spaces for the first row
    for (int i = 0; i < startDay; i++) {
        cout << "   ";
    }
    
    int daysInMonth = getDaysInMonth(month, year);
    
    // Print all days with proper formatting
    for (int day = 1; day <= daysInMonth; day++) {
        cout << setw(3) << day;
        
        currentDay++;
        
        // If it's Saturday (day 6), start a new line unless it's the last day
        if (currentDay % 7 == 0) {
            currentDay = 0;
            if (day != daysInMonth) {
                cout << endl;
            }
        }
    }
    
    cout << endl << endl;
    
    // Update startDay for the next month
    startDay = currentDay;
}







int main() {
    int year;
    int startDay;
    
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