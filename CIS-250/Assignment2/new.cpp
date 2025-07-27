#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function prototype for testing
void runTest(int userAge, const string &expectedMessage);

int main() {
    // Vector of test cases: {age, expectedMessage}
    vector<pair<int, string>> testCases = {
        {57, "There are 3 years left until your next decade birthday.\nHave fun with friends and family on your next birthday\n"},
        {119, "There is 1 year left until your next decade birthday.\nPlan a HUGE party for your decade birthday!\n"},
        {25, "There are 5 years left until your next decade birthday.\nYou should throw a party!\n"},
        {13, "There are 7 years left until your next decade birthday.\nKids birthdays should always be celebrated!\n"},
        {20, "There are 10 years left until your next decade birthday.\nHave fun with friends and family on your next birthday\n"},
        {10, "There are 10 years left until your next decade birthday.\nKids birthdays should always be celebrated!\n"},
        {17, "There are 3 years left until your next decade birthday.\nKids birthdays should always be celebrated!\n"},
        {18, "There are 2 years left until your next decade birthday.\nHave fun with friends and family on your next birthday\n"},
        {19, "There is 1 year left until your next decade birthday.\nPlan a HUGE party for your decade birthday!\n"},
        {29, "There is 1 year left until your next decade birthday.\nPlan a big party for your decade birthday!\n"}
    };

    // Run test cases
    for (const auto &testCase : testCases) {
        runTest(testCase.first, testCase.second);
    }

    return 0;
}

void runTest(int userAge, const string &expectedMessage) {
    // Simulate program logic
    int yearsLeftForDecade;
    yearsLeftForDecade = 10 - (userAge % 10);

    string output;

    // Making sure grammar is correct for different years left
    if (yearsLeftForDecade > 1) {
        output += "There are " + to_string(yearsLeftForDecade) + " years left until your next decade birthday.\n";
    } else {
        output += "There is " + to_string(yearsLeftForDecade) + " year left until your next decade birthday.\n";
    }

    // Part II
    if (userAge <= 17) {
        output += "Kids birthdays should always be celebrated!\n";
    }
    else if (userAge >= 18 && yearsLeftForDecade == 5) {
        output += "You should throw a party!\n";
    }
    else if (userAge >= 18 && yearsLeftForDecade == 1) {
        if (((userAge + yearsLeftForDecade) / 10) % 2 == 0) {
            output += "Plan a HUGE party for your decade birthday!\n";
        } else {
            output += "Plan a big party for your decade birthday!\n";
        }
    }
    else if (userAge >= 18) {
        output += "Have fun with friends and family on your next birthday\n";
    }

    // Check if output matches expected message
    cout << "Testing age: " << userAge << endl;
    if (output == expectedMessage) {
        cout << "Test passed!\n";
    } else {
        cout << "Test failed!\nExpected:\n" << expectedMessage << "Got:\n" << output;
    }
    cout << "------------------------------------\n";
}
