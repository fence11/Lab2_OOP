#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Aggregation (Faculty contains students)
class Student {
public:
    string name;
    Student(string n) : name(n) {}
};

class Faculty {
private:
    vector<Student*> students;

public:
    void addStudent(Student* s) {
        students.push_back(s);
    }

    void showStudents() const {
        for (const auto& s : students) {
            cout << s->name << endl;
        }
    }
};

// Composition (Library contains books)
class Book {
public:
    string title;
    Book(string t) : title(t) {}
};

class Library {
private:
    vector<Book*> books;

public:
    Library() {}
    ~Library() {
        for (auto book : books) {
            delete book;
        }
    }

    void addBook(Book* b) {
        books.push_back(b);
    }

    void showBooks() const {
        for (const auto& b : books) {
            cout << b->title << endl;
        }
    }
};

int main() {
    // Aggregation example
    Faculty faculty;
    Student s1("Arbuz"), s2("Arbuz");
    faculty.addStudent(&s1);
    faculty.addStudent(&s2);
    faculty.showStudents();

    // Composition example
    Library library;
    library.addBook(new Book("fdr assassination"));
    library.addBook(new Book("break good"));
    library.showBooks();  // Books will be deleted when the library is destroyed
}
