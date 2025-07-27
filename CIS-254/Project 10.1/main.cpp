/*
  Lynn T. Aung
  CIS - 254
  Project 10.1
*/

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
using namespace std;

// Adding Function Prototypes so I know what to add
void getProbsPerSet(int &);
void doOneSet(char, int, int &);
void printReport(int, int, int, int, int);
void printHeader(char);
void getMaxNum(int &);
void doOneProblem(char, int, int &);
void generateOperands(int &, int &, int);
void calculateCorrectAnswer(int, int, char, int &);
void checkAnswer(int, int, int &);

int main() {
    
    // Declare the number of correct answers
    // for each set
    int probsPerSet, correctInSet1 = 0, 
    correctInSet2 = 0, correctInSet3 = 0;
    
    // srand(static_cast<unsigned>(time(nullptr)));  // comment this out to submit to zyBooks
    getProbsPerSet(probsPerSet); 
    doOneSet('+', probsPerSet, correctInSet1);
    doOneSet('-', probsPerSet, correctInSet2);
    doOneSet('*', probsPerSet, correctInSet3);
    printReport(probsPerSet, correctInSet1, correctInSet2, 
        correctInSet3, correctInSet1 + correctInSet2 + 
        correctInSet3);
}

void getProbsPerSet(int &probsPerSet) {
    // Print out the question to get the input
    // for one question
    cout << "Enter problems per set: ";
    cin >> probsPerSet;
}

void doOneSet(char operation, int probsPerSet, int & correctPerSet) {

    printHeader(operation);

    int maxNum;
    getMaxNum(maxNum);

    // Call do one problem the number of times of
    // probs per set
    for (int i = 0; i < probsPerSet; i++) {
        doOneProblem(operation, maxNum, correctPerSet);
    }
}

void doOneProblem(char operation, int maxNum, int & correctPerSet) {

    int num1, num2, answer, correctAnswer;

    // Now, there's values in our variables in doOneProblem
    generateOperands(num1, num2, maxNum);
    calculateCorrectAnswer(num1, num2, operation, correctAnswer);

    // Print question and get answer
    cout << num1 << " " << operation << " " << num2 << " = ";
    cin >> answer;

    // Check answer
    checkAnswer(answer, correctAnswer, correctPerSet);
}

// Since we can't use global variables or return functions, we use
// pass-by-reference to change the variables in doOneProblem
void generateOperands(int &num1, int &num2, int maxNum) {
    // Generate numbers between 0 and the max number 
    num1 = rand() % (maxNum + 1);
    num2 = rand() % (maxNum + 1);

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
void checkAnswer(int userAnswer, int correctAnswer, int & correctPerSet) {
    if (userAnswer == correctAnswer) {
        cout << "correct" << endl;
        // If the answer is correct, we add to the correct
        // answers per set.
        correctPerSet++;
    } else {
        cout << "incorrect" << endl;
    }
}

void getMaxNum(int &maxNum) {
    // Get max number from users
    cout << "What is the maximum number for this set? ";
    cin >> maxNum;
}

void printHeader(char operation) {
    // We define difference headers 
    // for different operations
    if (operation == '+') {
        cout << endl;
        cout << "Set #1" << endl;
        cout << "----------" << endl;
    } else if (operation == '-') {
        cout << endl;
        cout << "Set #2" << endl;
        cout << "----------" << endl;
    } else if (operation == '*') {
        cout << endl;
        cout << "Set #3" << endl;
        cout << "----------" << endl;
    }
}

void printReport(int probsPerSet, int correctPerSet1, 
    int correctPerSet2, int correctPerSet3, 
    int totalCorrect) {

    // Calculate the total number of problems
    int totalProbs = probsPerSet * 3;

    cout << endl;

    // Print in clean format
    cout << "Set#1:  You got " << correctPerSet1 << 
    " correct out of " << 
    probsPerSet << " for "  << fixed << setprecision(1) <<
    static_cast<double>(correctPerSet1) / probsPerSet * 100 << 
    "%" << endl;

    cout << "Set#2:  You got " << correctPerSet2 << 
    " correct out of " << probsPerSet << 
    " for "  << fixed << setprecision(1) <<
    static_cast<double>(correctPerSet2) / probsPerSet * 100 << 
    "%" << endl;

    cout << "Set#3:  You got " << correctPerSet3 << 
    " correct out of " << probsPerSet << 
    " for "  << fixed << setprecision(1) <<
    static_cast<double>(correctPerSet3) / probsPerSet * 100 << 
    "%" << endl;

    cout << "Overall you got " << totalCorrect << 
    " correct out of " << totalProbs << 
    " for "  << fixed << setprecision(1) <<
    static_cast<double>(totalCorrect) / totalProbs * 100 << 
    "%" << endl;
}