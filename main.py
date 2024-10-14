class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}"


class Student(Person):
    student_id_counter = 1

    def __init__(self, name, email, major):
        super().__init__(name, email)
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.major = major
        self.graduated = False

    def graduate(self):
        self.graduated = True

    def get_details(self):
        return f"ID: {self.student_id}, Name: {self.name}, Major: {self.major}, Graduated: {self.graduated}"


class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_departments(self):
        return [dept.get_details() for dept in self.departments]

    def get_students(self):
        students = []
        for department in self.departments:
            students.extend(department.students)
        return students

    def get_details(self):
        return f"Faculty: {self.name}"


class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return [student.get_details() for student in self.students]

    def get_details(self):
        return f"Department: {self.name}, Students: {len(self.students)}"


class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculties = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def add_student_to_department(self, student_id, department_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        department = next((d for d in sum([f.departments for f in self.faculties], []) if d.id == department_id), None)
        if student and department:
            department.add_student(student)
            print(f"Student {student_id} assigned to Department {department_id}.")
        else:
            print("Invalid student or department ID.")

    def graduate_student(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.graduate()
            print(f"Student {student_id} has graduated.")
        else:
            print("Invalid student ID.")

    def display_graduate_students(self):
        graduates = [s for s in self.students if s.graduated]
        if graduates:
            print("\nGraduate Students:")
            for student in graduates:
                print(f"ID: {student.student_id}, Name: {student.name}, Major: {student.major}")
        else:
            print("\nNo graduate students found.")

    def display_non_graduate_students(self):
        non_graduates = [s for s in self.students if not s.graduated]
        if non_graduates:
            print("\nCurrent Non-Graduate Students:")
            for student in non_graduates:
                faculty = next(f for f in self.faculties if any(dept for dept in f.departments if student in dept.students))
                department = next(dept for dept in faculty.departments if student in dept.students)
                print(f"ID: {student.student_id}, Name: {student.name}, Major: {student.major}, Faculty: {faculty.name}, Department: {department.name}")
        else:
            print("\nNo non-graduate students found.")

    def display_faculty_and_students(self, faculty_id):
        faculty = next((f for f in self.faculties if f.id == faculty_id), None)
        if faculty:
            print(f"\nFaculty: {faculty.name}")
            students = faculty.get_students()
            if students:
                print("Enrolled Students:")
                for student in students:
                    department = next(dept for dept in faculty.departments if student in dept.students)
                    print(f"ID: {student.student_id}, Name: {student.name}, Major: {student.major}, Department: {department.name}")
            else:
                print("No students enrolled in this faculty.")
        else:
            print("Invalid faculty ID.")


def menu():
    university = University("Example University")

    while True:
        print("\n--- University Menu ---")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Create Department")
        print("4. Assign Student to Department")
        print("5. Graduate Student")
        print("6. Display All Graduate Students")
        print("7. Display All Current Non-Graduate Students")
        print("8. Display Faculty and Enrolled Students")
        print("0. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            major = input("Enter student major: ")
            student = Student(name, email, major)
            university.add_student(student)
            print(f"Student {name} added with ID {student.student_id}.")

        elif choice == '2':
            name = input("Enter faculty name: ")
            faculty_id = len(university.faculties) + 1
            faculty = Faculty(faculty_id, name)
            university.add_faculty(faculty)
            print(f"Faculty {name} added with ID {faculty.id}.")

        elif choice == '3':
            department_name = input("Enter department name: ")
            department_id = len(sum([f.departments for f in university.faculties], [])) + 1
            faculty_id = int(input("Enter faculty ID: "))
            faculty = next((f for f in university.faculties if f.id == faculty_id), None)
            if faculty:
                department = Department(department_id, department_name)
                faculty.add_department(department)
                print(f"Department {department_name} added to Faculty {faculty.name} with ID {department.id}.")
            else:
                print("Invalid faculty ID.")

        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            department_id = int(input("Enter department ID: "))
            university.add_student_to_department(student_id, department_id)

        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            university.graduate_student(student_id)

        elif choice == '6':
            university.display_graduate_students()

        elif choice == '7':
            university.display_non_graduate_students()

        elif choice == '8':
            faculty_id = int(input("Enter faculty ID: "))
            university.display_faculty_and_students(faculty_id)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


menu()
