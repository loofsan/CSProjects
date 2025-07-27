/*
  Lynn T. Aung
  CIS - 254
  Project 4.4
  Cost Rate Structure for Calls
*/



#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Make constant variables on the discounts and rates
    const double REGULAR_RATE = 0.40;       
    const double TIME_DISCOUNT = 0.50;      
    const double DURATION_DISCOUNT = 0.15;     
    const double FEDERAL_TAX = 0.04;        
    const int DISCOUNT_VALID = 1800;         
    const int DISCOUNT_INVALID = 800;          
    const int LONG_CALL_MINUTES = 60;        
    
    int startTime;
    int callDuration;
    
    // Get input on the start time and length of call.
    cout << "Enter start time: ";
    cin >> startTime;
    cout << "Enter length of call in minutes: ";
    cin >> callDuration;
    
   
    double grossCost = callDuration * REGULAR_RATE;
    cout << "The gross cost is $" << setprecision(2) << fixed << grossCost << endl;
    
   
    double netCost = grossCost;
    
    
    if (startTime >= DISCOUNT_VALID || startTime < DISCOUNT_INVALID) {
        netCost *= (1 - TIME_DISCOUNT);
    }
    
   
    if (callDuration > LONG_CALL_MINUTES) {
        netCost *= (1 - DURATION_DISCOUNT);
    }
    
    
    netCost *= (1 + FEDERAL_TAX);
    
    cout << "The net cost is $" << netCost << endl;
    
    return 0;
}