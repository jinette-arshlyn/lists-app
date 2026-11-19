def add_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")

    student = {
        'name': name,
        'age': age,
        'grade': grade
    }

    with open('students.txt', 'a') as file:
        file.write(f"{student['name']},{student['age']},{student['grade']}\n")

    print(f"Student {name} added successfully!")

def view_students():
    try:
        with open('students.txt', 'r') as file:
            students = file.readlines()
            if not students:
                print("No students found.")
                return
            for student in students:
                name, age, grade = student.strip().split(',')
                print(f"Name: {name}, Age: {age}, Grade: {grade}")
    except FileNotFoundError:
        print("No students found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

