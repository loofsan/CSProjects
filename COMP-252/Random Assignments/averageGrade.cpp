#include <iostream>
using namespace std;

int main() 
{
    int grade, sum=0, limit;
    cout << "How many grades do you want to put in?" << endl;
    cin >> limit;
    for (int i = 0; i < limit; i++) {

        do {
            cout << "Enter grade " << i + 1 << ": ";
            cin >> grade;

        } while(grade<1 || grade>5);

        sum += grade;
    }
    cout << "Sum: " << sum << endl;
    cout << "Average Grade: " << (float)sum/limit << endl;

    return 0;
}