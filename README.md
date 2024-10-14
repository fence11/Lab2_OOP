# Lab2_OOP

Student Management System for a University

## Functionality

- **Add Student**: Add new students with their name, email, and major.
- **Add Faculty**: Add new faculty with a unique ID and name.
- **Create Department**: Add new departments to a specific faculty.
- **Assign Student to Department**: Enroll students in a department.
- **Graduate Student**: Mark a student as a graduate.
- **Display Graduate Students**: View a list of all graduate students.
- **Display Current Non-Graduate Students**: View a list of students who are yet to graduate along with their faculty and department details.
- **Display Faculty and Enrolled Students**: View all students enrolled under a specific faculty.

## Classes and Methods

### 1. **Person**
Base class to represent common properties for both students and faculty.

#### Methods:
- `__init__(self, name, email)`: Initializes a person with a name and email.
- `get_details(self)`: Returns the name and email of the person.

### 2. **Student** (inherits from `Person`)
Represents a student with a major, GPA, courses enrolled, and graduation status.

#### Methods:
- `__init__(self, name, email, major)`: Initializes a student with a name, email, and major, assigns a unique student ID, and sets default GPA and graduation status.
- `enroll(self, course)`: Enrolls the student in a course.
- `graduate(self)`: Marks the student as graduated.
- `get_details(self)`: Returns the student's details including name, email, major, GPA, and graduation status.

### 3. **Faculty**
Represents a faculty that manages various departments.

#### Methods:
- `__init__(self, id, name)`: Initializes a faculty with an ID and name, and creates an empty list of departments.
- `add_department(self, department)`: Adds a department to the faculty.
- `get_departments(self)`: Returns the list of departments in the faculty.
- `get_details(self)`: Returns the faculty name.

### 4. **Department**
Represents a department that holds students and courses.

#### Methods:
- `__init__(self, id, name)`: Initializes a department with an ID and name, and creates empty lists for students and courses.
- `add_student(self, student)`: Adds a student to the department.
- `add_course(self, course)`: Adds a course to the department.
- `get_students(self)`: Returns a list of students in the department.
- `get_courses(self)`: Returns a list of courses in the department.
- `get_details(self)`: Returns department details such as name, number of students, and courses.

### 5. **University**
The main class that manages all students, faculties, and departments.

#### Methods:
- `__init__(self, name)`: Initializes the university with a name and creates empty lists for students, faculties, and courses.
- `add_student(self, student)`: Adds a student to the university.
- `add_faculty(self, faculty)`: Adds a faculty to the university.
- `create_course(self, course)`: Creates a course in the university.
- `add_student_to_department(self, student_id, department_id)`: Assigns a student to a department by their ID.
- `display_all_faculties(self)`: Displays all faculties in the university.
- `display_departments_in_faculty(self, faculty_id)`: Displays all departments under a specific faculty.
