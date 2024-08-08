#include <iostream>
using namespace std;

int main() 
{
    //weight / height * height
    // Underweight < 18.5
    // Normal Weight 18.5 - 24.9
    // Overweight > 25
    cout << "Hello, please enter your height(m) and weight(kg): ";
    float weight, height;
    cin >> height >> weight;

    float bmi = weight / (height * height);

    if (bmi < 18.5)
        cout << "You are underweight." << endl;
    else if (bmi > 25)
        cout << "You are overweight." << endl;
    else
        cout << "You have a normal weight." << endl;
    
    cout << "Your BMI is " << bmi << endl;
    return 0;
}