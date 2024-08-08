#include <iostream>
using namespace std;

int recursive_sum(int m, int n) {
    if (m == n) 
        return m;
    return m + recursive_sum(m+1,n);
}




// Sum numbers between m - n
int main() 
{
    int m, n;
    cout << "m: ";
    cin >> m;
    cout << "n: ";
    cin >> n;
    
    if (m > n) {
        int temp = m;
        m = n;
        n = temp;
    }

    cout << "Sum = " << recursive_sum(m,n) << endl;

    /*
    int sum = 0;
    for (int i=m;i<=n;i++) {
        sum += i;
    }
    cout << "Sum = " << sum << endl;
    */

    return 0;
}