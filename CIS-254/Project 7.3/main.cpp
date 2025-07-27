/*
  Lynn T. Aung
  CIS - 254
  Project 7.3
  Number Of Words
*/
#include <iostream>
#include <fstream>
using namespace std;


int main() {

    string userInput;
    
    do {
        cout << "Enter the filename: ";
        cin >> userInput;
        
        if (userInput == "quit") {
            break;
        }
        
        // Try opening the file
        ifstream inputFile(userInput);
        
        // Re-prompt if we can't open file
        if (!inputFile.is_open()) {
            cout << "Couldn't open file." << endl;
            continue;
        }
        
        
        string word;
        int wordCount = 0;
        
        // Read each word into the string variable
        while (inputFile >> word) {
            wordCount++;
        }
        
        // Close the file
        inputFile.close();
        
        cout << "The file has " << wordCount << " words." << endl;
        
    } while (userInput != "quit");


    return 0;
}