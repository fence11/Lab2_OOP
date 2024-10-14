#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    virtual string getRole() const = 0; // Pure virtual function
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

class Administrator : public Person {
public:
    string getRole() const override {
        return "Administrator";
    }
};

int main() {
    Person* person1 = new Student();
    Person* person2 = new Teacher();
    Person* person3 = new Administrator();

    cout << "Role of person1: " << person1->getRole() << endl;
    cout << "Role of person2: " << person2->getRole() << endl;
    cout << "Role of person3: " << person3->getRole() << endl;

    return 0;
}
