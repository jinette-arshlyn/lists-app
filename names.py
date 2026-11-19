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

add_student()