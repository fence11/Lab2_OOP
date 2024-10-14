#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    Person(string n = "", int a = 0) : name(n), age(a) {}
    void showPerson() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Student : public Person {
protected:
    int studentID;
    string faculty;

public:
    Student(string n = "", int a = 0, int id = 0, string f = "") : Person(n, a), studentID(id), faculty(f) {}
    void showStudent() const {
        showPerson();
        cout << "StudentID: " << studentID << ", Faculty: " << faculty << endl;
    }
};

class Employee {
protected:
    int employeeID;
    double salary;

public:
    Employee(int id = 0, double sal = 0.0) : employeeID(id), salary(sal) {}
    void showEmployee() const {
        cout << "EmployeeID: " << employeeID << ", Salary: " << salary << endl;
    }
};

class StudentEmployee : public Student, public Employee {
public:
    StudentEmployee(string n, int a, int sID, string f, int eID, double sal)
        : Student(n, a, sID, f), Employee(eID, sal) {}

    void showStudentEmployee() const {
        showStudent();
        showEmployee();
    }
};

int main() {
    StudentEmployee se("John Doe", 21, 12345, "Engineering", 1001, 50000);
    se.showStudentEmployee();
}
