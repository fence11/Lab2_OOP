#include <iostream>
using namespace std;

class Student {
private:
    int credits;

public:
    Student(int c = 0) : credits(c) {}

    // Unary operator overload
    Student& operator++() { // Prefix increment
        ++credits;
        return *this;
    }

    Student& operator--() { // Prefix decrement
        --credits;
        return *this;
    }

    // Operator overload
    Student& operator+=(const Student& s) {
        credits += s.credits;
        return *this;
    }

    int getCredits() const {
        return credits;
    }
};

int main() {
    Student s1(10), s2(5);
    ++s1;       
    --s2;       
    s1 += s2; 

    cout << "s1's credits: " << s1.getCredits() << endl; // Output: 15
    cout << "s2's credits: " << s2.getCredits() << endl; // Output: 4
}
