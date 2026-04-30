/*
  Lynn T. Aung
  CIS - 254
  Project 9.1
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Adding Function Prototypes so I know what to add
void doOneSet(char);
void doOneProblem(char);
void generateOperands(int &, int &);
void checkAnswer(int, int);
void calculateCorrectAnswer(int, int, char, int &);

int main() {

    // srand(static_cast<unsigned>(time(nullptr)));    
    doOneSet('+');
    doOneSet('-');
    doOneSet('*');
    
    return 0;
}

void doOneSet(char operation) {
    // Call do one problem 5 times
    for (int i = 0; i < 5; i++) {
        doOneProblem(operation);
    }
}

void doOneProblem(char operation) {

    int num1, num2, answer, correctAnswer;

    // Now, there's values in our variables in doOneProblem
    generateOperands(num1, num2);
    calculateCorrectAnswer(num1, num2, operation, correctAnswer);

    // Print question and get answer
    cout << num1 << " " << operation << " " << num2 << " = ";
    cin >> answer;

    // Check answer
    checkAnswer(answer, correctAnswer);
}

// Since we can't use global variables or return functions, we use
// pass-by-reference to change the variables in doOneProblem
void generateOperands(int &num1, int &num2) {
    // Generate numbers between 0 and 100
    num1 = rand() % 101;
    num2 = rand() % 101;

}

// Use pass-by-reference to change the data in doOneProblem()
void calculateCorrectAnswer(int num1, int num2, char operation, int &correctAnswer) {
    // Use if-else block to check operation and do the respective operation
    if (operation == '+') {
        correctAnswer = num1 + num2;
    } else if (operation == '-') {
        correctAnswer = num1 - num2;
    } else if (operation == '*') {
        correctAnswer = num1 * num2;
    }
}

// Checks if the answer is correct or not
void checkAnswer(int userAnswer, int correctAnswer) {
    if (userAnswer == correctAnswer) {
        cout << "correct" << endl;
    } else {
        cout << "incorrect" << endl;
    }
}