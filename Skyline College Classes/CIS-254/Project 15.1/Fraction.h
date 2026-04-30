// Fraction.h
// Lynn T. Aung
// CIS - 254
// 4/27/2025
// Project 15.1
// Professor Dave Harden
// File: Fraction.h
//
// Brief description:
//     Defines a Fraction class to represent non-negative rational numbers
//     stored in reduced form.  Provides arithmetic operations, equality
//     comparison, and printing in "numerator/denominator" format.
//
// Public member function prototypes (with pre/post):
//     Fraction();  
//         Pre:  none
//         Post: this fraction is 0/1
//
//     Fraction(int num, int denom);
//         Pre:  denom != 0
//         Post: this fraction is num/denom, reduced to lowest terms
//
//     Fraction addedTo(const Fraction& rhs) const;
//         Pre:  none
//         Post: returns a new Fraction equal to this + rhs, in lowest terms
//
//     Fraction subtract(const Fraction& rhs) const;
//         Pre:  none
//         Post: returns a new Fraction equal to this − rhs, in lowest terms
//
//     Fraction multipliedBy(const Fraction& rhs) const;
//         Pre:  none
//         Post: returns a new Fraction equal to this × rhs, in lowest terms
//
//     Fraction dividedBy(const Fraction& rhs) const;
//         Pre:  rhs.numerator != 0
//         Post: returns a new Fraction equal to this ÷ rhs, in lowest terms
//
//     bool isEqualTo(const Fraction& rhs) const;
//         Pre:  none
//         Post: returns true iff this and rhs represent the same value
//
//     void print() const;
//         Pre:  none
//         Post: printed to cout in "numerator/denominator" form
//

#ifndef FRACTION_H
#define FRACTION_H

#include <cassert>
#include <iostream>

class Fraction
{
private:
    int numerator;
    int denominator;

    void simplify();

public:
    Fraction();
    Fraction(int num, int denom);

    Fraction addedTo(const Fraction & rhs) const;
    Fraction subtract(const Fraction & rhs) const;
    Fraction multipliedBy(const Fraction & rhs) const;
    Fraction dividedBy(const Fraction & rhs) const;

    bool isEqualTo(const Fraction & rhs) const;

    void print() const;
};

#endif // FRACTION_H
