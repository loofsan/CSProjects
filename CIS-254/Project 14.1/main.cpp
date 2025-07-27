/*
  Lynn T. Aung
  CIS - 254
  4/27/2025
  Professor Dave Harden
  Project 14.1
  
  This program defines a Fraction class to represent fractions with integer
  numerators and denominators. It provides operations to set a fraction,
  add, subtract, multiply, and divide fractions (without reducing them),
  compare two fractions for equality via cross-multiplication, and print
  a fraction in "numerator/denominator" form. The main function demonstrates
  these operations on two sample fractions.
  
  Input: Two fractions specified in code via f1.set(9, 8) and f2.set(2, 3)
         (i.e., 9/8 and 2/3)

  Output: 
    A formatted display of the operation and its result.
*/

#include <iostream>
using namespace std;


// Class Declaration
class Fraction {

    // Declaring member variables
    private:
        int numerator;
        int denominator;
    
    // Declaring public functions
    public:
        void set(int numerator, int denominator);
        Fraction addedTo(Fraction operand);
        Fraction subtract(Fraction operand);
        Fraction multipliedBy(Fraction operand);
        Fraction dividedBy(Fraction operand);
        bool isEqualTo(Fraction obj2);
        void print();
};





// This function will set the function values inside the object
void Fraction::set(int numerator, int denominator) {
    this->numerator = numerator;
    this->denominator = denominator;
}





// Addition operation of fractions
Fraction Fraction::addedTo(Fraction operand) {

    Fraction result;

    result.denominator = denominator * operand.denominator;

    result.numerator = (numerator * operand.denominator) + 
        (denominator * operand.numerator);
    
    return result;
}





// Subtraction operation of fractions
Fraction Fraction::subtract(Fraction operand) {

    Fraction result;

    result.denominator = denominator * operand.denominator;

    result.numerator = (numerator * operand.denominator) - 
        (denominator * operand.numerator);

    return result;
}





// Multiplication operation of fractions
Fraction Fraction::multipliedBy(Fraction operand) {

    Fraction result;

    result.numerator = numerator * operand.numerator;
    result.denominator = denominator * operand.denominator;

    return result;
}





// Division operation of fractions
Fraction Fraction::dividedBy(Fraction operand) {

    Fraction result;

    result.numerator = numerator * operand.denominator;
    result.denominator = denominator * operand.numerator;

    return result;
}





// Checks if two functions are equal to each other
bool Fraction::isEqualTo(Fraction operand) {

    if (numerator * operand.denominator == denominator * operand.numerator) {
        return true;
    }

    return false;
}





// Prints a function in the format, [numerator]/[denominator]
void Fraction::print() {
    cout << numerator << "/" << denominator;
}






int main() {

    Fraction f1;
    Fraction f2;
    Fraction result;

    f1.set(9, 8);
    f2.set(2, 3);

    cout << "The product of ";
    f1.print();
    cout << " and ";
    f2.print();
    cout << " is ";
    result = f1.multipliedBy(f2);
    result.print();
    cout << endl;

    cout << "The quotient of ";
    f1.print();
    cout << " and ";
    f2.print();
    cout << " is ";
    result = f1.dividedBy(f2);
    result.print();
    cout << endl;

    cout << "The sum of ";
    f1.print();
    cout << " and ";
    f2.print();
    cout << " is ";
    result = f1.addedTo(f2);
    result.print();
    cout << endl;

    cout << "The difference of ";
    f1.print();
    cout << " and ";
    f2.print();
    cout << " is ";
    result = f1.subtract(f2);
    result.print();
    cout << endl;

    if (f1.isEqualTo(f2)){
        cout << "The two Fractions are equal." << endl;
    } else {
        cout << "The two Fractions are not equal." << endl;
    }

    return 0;
}