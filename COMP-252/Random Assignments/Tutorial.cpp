#include <string>
#include <iostream>
using std::cin;
using std::cout;
using std::string;
using std::endl;
int main() 
{
    string str("Hello world");
    for (auto c : str) 
    {
        cout << c << endl;
    }
    return 0;
}
