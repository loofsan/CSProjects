// Fraction.cpp
// Lynn T. Aung
// CIS - 254
// 4/27/2025
// Project 15.1
// Professor Dave Harden
// File: Fraction.cpp
//
// Class Invariant:
//     - numerator and denominator are always non-negative.
//     - denominator is never zero.
//     - fraction is always stored in lowest terms (gcd = 1).
//
// Private data members:
//     numerator   holds the fraction’s numerator
//     denominator holds the fraction’s denominator
//
// Private helper:
//     simplify() reduces the calling object to lowest terms.
//

#include "Fraction.h"





// simplify
//     Reduces this->numerator/this->denominator by trial‐division GCF.
//     Called by constructors and all mutating operations.
//     Pre:  denominator != 0
//     Post: numerator/denominator in lowest terms; if numerator==0, denom=1.
void Fraction::simplify()
{
    if (numerator == 0)
    {
        denominator = 1;
        return;
    }

    int gcf = 1;
    int limit = numerator < denominator ? numerator : denominator;

    for (int i = 2; i <= limit; ++i)
    {
        if (numerator % i == 0 && denominator % i == 0)
        {
            gcf = i;
        }
    }

    numerator   /= gcf;
    denominator /= gcf;
}





// Fraction()
//     Default constructor.
//     Pre:  none
//     Post: this fraction is 0/1
Fraction::Fraction()
    : numerator(0), denominator(1)
{
}





// Fraction(int, int)
//     Parameterized constructor.
//     Pre:  denom != 0
//     Post: this fraction is num/denom, reduced
Fraction::Fraction(int num, int denom)
    : numerator(num), denominator(denom)
{
    assert(denominator != 0);
    simplify();
}





// addedTo
//     Returns this + rhs in lowest terms.
//     Pre:  none
//     Post: result is reduced
Fraction Fraction::addedTo(const Fraction & rhs) const
{
    Fraction result;
    result.numerator   = numerator * rhs.denominator
                       + denominator * rhs.numerator;
    result.denominator = denominator * rhs.denominator;
    result.simplify();
    return result;
}





// subtract
//     Returns this − rhs in lowest terms.
//     Pre:  none
//     Post: result is reduced
Fraction Fraction::subtract(const Fraction & rhs) const
{
    Fraction result;
    result.numerator   = numerator * rhs.denominator
                       - denominator * rhs.numerator;
    result.denominator = denominator * rhs.denominator;
    result.simplify();
    return result;
}





// multipliedBy
//     Returns this × rhs in lowest terms.
//     Pre:  none
//     Post: result is reduced
Fraction Fraction::multipliedBy(const Fraction & rhs) const
{
    Fraction result;
    result.numerator   = numerator * rhs.numerator;
    result.denominator = denominator * rhs.denominator;
    result.simplify();
    return result;
}





// dividedBy
//     Returns this ÷ rhs in lowest terms.
//     Pre:  rhs.numerator != 0
//     Post: result is reduced
Fraction Fraction::dividedBy(const Fraction & rhs) const
{
    Fraction result;
    result.numerator   = numerator * rhs.denominator;
    result.denominator = denominator * rhs.numerator;
    result.simplify();
    return result;
}





// isEqualTo
//     Compares this and rhs for equality via cross-multiplication.
//     Pre:  none
//     Post: returns true iff values match
bool Fraction::isEqualTo(const Fraction & rhs) const
{
    return numerator * rhs.denominator
         == denominator * rhs.numerator;
}





// print
//     Outputs the fraction in "numerator/denominator" form.
//     Pre:  none
//     Post: printed to std::cout
void Fraction::print() const
{
    std::cout << numerator << "/" << denominator;
}
