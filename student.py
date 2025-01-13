class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students.values():
                print(student)

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id not in self.students:
            print("Student ID not found.")
        else:
            if name:
                self.students[student_id].name = name
            if age:
                self.students[student_id].age = age
            if grade:
                self.students[student_id].grade = grade
            print("Student updated successfully.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")


# Main program
def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            sms.add_student(student_id, name, age, grade)

        elif choice == "2":
            print("\nStudent List:")
            sms.view_students()

        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            print("Leave fields blank if no changes.")
            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            grade = input("Enter new Grade: ")
            sms.update_student(student_id, name, age, grade)

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()