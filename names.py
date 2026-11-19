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

add_student()
view_students()
