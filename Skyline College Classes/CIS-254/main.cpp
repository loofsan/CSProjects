#include <iostream>
using namespace std;


#include <iostream>
using namespace std;
const double LB_PER_KG = 2.2;

double KgsToLbs(double kilograms) {
   double pounds;
   pounds = kilograms * LB_PER_KG;
   return pounds;
}

int main() {
   double pounds;
   pounds = KgsToLbs(10);
   cout << pounds;
   return 0;
}