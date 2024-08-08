#include <iostream>
using namespace std;

int main() 
{
    cout << "Enter any kind of integer: ";
    int answer;
    cin >> answer;
    if(answer%2 == 0) 
        cout << "Hello, your integer is even." << endl;
    else
        cout << "Hello, your integer is odd." << endl;
    
    cout << "Thanks, Bye." << endl;
}