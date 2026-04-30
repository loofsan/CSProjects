#include <iostream>
using namespace std;


class ContactCard {
    private:
        string name;
        string email;

    public:
        ContactCard(string name, string email="unknown"): name(name), email(email) {};
        bool operator==(const ContactCard& other) const {
            return this->name == other.name && this->email == other.email;
        }
        string getName() const { return name; }
        string getEmail() const { return email; }
        void setName(string name) { this->name = name; }
        void setEmail(string email) { this->email = email; }
};

int main() {

    ContactCard c1("Joe", "email1");
    ContactCard c2("Lynn");

    cout << c1.getName() << " " << c1.getEmail() << endl;
    cout << c2.getName() << " " << c2.getEmail() << endl;
    c2.setEmail("email2");
    cout << c2.getName() << " " << c2.getEmail() << endl;
    c2.setEmail("email1");
    c2.setName("Joe");
    cout << (c1 == c2 ? "True" : "False") << endl;

    const int newad = 10;
    cout << newad;

}