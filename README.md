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

## Program Structure

The program consists of several key classes:

1. **Person**: The base class for storing basic details like name and email.
2. **Student**: Inherits from `Person`, stores additional information like major, graduation status, and a unique student ID.
3. **Faculty**: Represents a faculty and holds references to its departments.
4. **Department**: Represents a department and holds a list of enrolled students.
5. **University**: Main class for managing the university, linking students, faculties, and departments.
