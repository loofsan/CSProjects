// Lynn T. Aung
// 4 - 8 - 2024
// COMP - 252
// Assignment 5 - Balanced Parantheses

#include <iostream>
#include <stack>
using namespace std;

bool isBalanced(const string &str) {
    stack<char> stringStack;

     for (char c : str) {
        // Push into stack when we see opening parantheses
        if (c == '(' || c == '[' || c == '{') 
        {
            stringStack.push(c);
        } 
        else if (c == ')' || c == ']' || c == '}') 
        {
            if (stringStack.empty()) 
            {   // If there are closing parantheses while the list is empty, false
                return false; 
            }
            // First get the char on the top of the stack
            char top = stringStack.top();
            // Remove it as we already recorded the top in var top
            stringStack.pop();
            // Check if valid
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) 
            {
                return false; 
            }
        }
    }

    return stringStack.empty(); 
}

int main () {

    cout << isBalanced("(@%&![()$%&])") << endl;
    cout << "Output: 1" << endl;
    cout << isBalanced("{{[[[#(a)]]]}}") << endl;   
    cout << "Output: 1" << endl;
    cout << isBalanced(")(}{][") << endl;  
    cout << "Output: 0" << endl;
    cout << isBalanced("{?>>2^%&]**}") << endl;  
    cout << "Output: 0" << endl;
    cout << isBalanced("(n)([()]&#b{5})") << endl;
    cout << "Output: 1" << endl; 
    cout << isBalanced("{({[yes})]}") << endl;   
    cout << "Output: 0" << endl;  
    cout << isBalanced("{]") << endl;   
    cout << "Output: 0" << endl;  
    cout << isBalanced("7ghb00") << endl;   
    cout << "Output: 1" << endl;  

    return 0;
}

