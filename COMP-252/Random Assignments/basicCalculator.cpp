#include <iostream>
using namespace std;

int main()
{
    cout << "**Lynn's Calculator**\n" << endl;
    bool flag = true;
    while (flag) 
    {
        float num1, num2;
        char operation;
        cin >> num1 >> operation>> num2;

        switch (operation) // The many functions the operation value can have
        {
        case '-':cout << num1 << operation << num2 << "=" << num1 - num2 << "\n"; break;
        case '+':cout << num1 << operation << num2 << "=" << num1 + num2 << "\n"; break;
        case '*':cout << num1 << operation << num2 << "=" << num1 * num2 << "\n"; break;
        case '/':cout << num1 << operation << num2 << "=" << num1 / num2 << "\n"; break;
        case '%':
            bool isNum1Int, isNum2Int;
            isNum1Int = ( (int)num1 == num1 );
            isNum2Int = ( (int)num2 == num2 );

            if (isNum1Int && isNum2Int) 
                cout << num1 << operation << num2 << "=" << (int) num1 % (int) num2;
            else 
                cout << "Not valid!" << endl;
            break;
        default:cout << "Not valid operation!" << endl; // What happens if the user doesn't use any of the
                                                        // variables above.
        }

        if (num1 == 0 && num2 == 0) // Keeps the function running until the user puts in 0 and 0.
        {
            flag = false;
            cout << "Calculator has stopped." << endl;
        }
    }
    return 0;
}