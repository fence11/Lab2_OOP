#include <iostream>
using namespace std;

class Person {
public:
    virtual string getRole() const = 0;  // Pure virtual function
};

class Student : public Person {
public:
    string getRole() const override {
        return "Student";
    }
};

class Teacher : public Person {
public:
    string getRole() const override {
        return "Teacher";
    }
};

// polymorphism to print role
void printRole(const Person* p) {
    cout << "Role: " << p->getRole() << endl;
}

int main() {
    Person* p = new Student();  // create a Student object
    printRole(p);

    p = new Teacher();  // create a Teacher object
    printRole(p);

    return 0;
}
