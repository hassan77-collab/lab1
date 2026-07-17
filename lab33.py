
students = {}

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()
    
    # Prevent duplicate Student IDs
    if student_id in students:
        print("Error: This Student ID already exists!")
        return
        
    name = input("Enter Student Name: ").strip()
    if not name:
        print("Error: Student name cannot be empty!")

        return

    try:
        grade = float(input("Enter Student Grade (0 to 100): "))
        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100!")
            return
    except ValueError:
        print("Error: Please enter a valid numerical grade!")
        return


    students[student_id] = {"name": name, "grade": grade}
    print(f"Student '{name}' added successfully.")

def show_all_students():
    print("\n--- Show All Students ---")
    if not students:
        print("No students registered yet.")
        return
        
    for s_id, info in students.items():
        print(f"ID: {s_id} | Name: {info['name']} | Grade: {info['grade']}")

def search_student():
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ").strip()
    
    if student_id in students:
        info = students[student_id]
        print(f"Student Found -> ID: {student_id} | Name: {info['name']} | Grade: {info['grade']}")
    else:

        print("Sorry, no student found with this ID.")

def update_grade():
    print("\n--- Update Student Grade ---")
    student_id = input("Enter Student ID: ").strip()
    
    if student_id in students:
        try:
            new_grade = float(input("Enter New Grade: "))
            if new_grade < 0 or new_grade > 100:
                print("Error: Grade must be between 0 and 100!")
                return
            students[student_id]['grade'] = new_grade
            print("Grade updated successfully.")
        except ValueError:

            print("Error: Invalid input for grade.")
    else:
        print("Error: Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()
    
    if student_id in students:
        deleted_student = students.pop(student_id)
        print(f"Student '{deleted_student['name']}' deleted successfully.")
    else:
        print("Error: Student not found.")

def calculate_average():
    print("\n--- Calculate Average Grade ---")
    if not students:

        print("No students available to calculate average.")
        return
        
    total_grades = sum(info['grade'] for info in students.values())
    average = total_grades / len(students)
    print(f"The average grade of all students is: {average:.2f}")

def show_best_student():
    print("\n--- Show Best Student ---")
    if not students:
        print("No students registered yet.")
        return
        
    best_id = max(students, key=lambda s_id: students[s_id]['grade'])
    best_student = students[best_id]
    print(f"Highest grade goes to: {best_student['name']} (ID: {best_id}) with Grade: {best_student['grade']}")

def show_worst_student():
    print("\n--- Show Worst Student ---")
    if not students:
        print("No students registered yet.")
        return
        
    worst_id = min(students, key=lambda s_id: students[s_id]['grade'])
    worst_student = students[worst_id]
    print(f"Lowest grade goes to: {worst_student['name']} (ID: {worst_id}) with Grade: {worst_student['grade']}")

def show_total_students():
    print("\n--- Total Number of Students ---")
    print(f"Total students registered in the system: {len(students)}")

def show_passed_students():

    print("\n--- Show Passed Students (60 or above) ---")
    passed = {s_id: info for s_id, info in students.items() if info['grade'] >= 60}
    
    if not passed:
        print("No students have passed.")
        return
        
    for s_id, info in passed.items():
        print(f"ID: {s_id} | Name: {info['name']} | Grade: {info['grade']}")

def show_failed_students():
    print("\n--- Show Failed Students (Less than 60) ---")
    failed = {s_id: info for s_id, info in students.items() if info['grade'] < 60}
    
    if not failed:
        print("No students have failed.")

        return
        
    for s_id, info in failed.items():
        print(f"ID: {s_id} | Name: {info['name']} | Grade: {info['grade']}")

def main():
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student by ID")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Calculate Average Grade")
        print("7. Show Best Student")
        print("8. Show Worst Student")
        print("9. Show Total Number of Students")

        print("10. Show Passed Students")
        print("11. Show Failed Students")
        print("12. Exit")
        print("===========================================")
        
        choice = input("Please select an option (1-12): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_grade()
        elif choice == '5':
            delete_student()
        elif choice == '6':

            calculate_average()
        elif choice == '7':
            show_best_student()
        elif choice == '8':
            show_worst_student()
        elif choice == '9':
            show_total_students()
        elif choice == '10':
            show_passed_students()
        elif choice == '11':
            show_failed_students()
        elif choice == '12':
            print("\nProgram terminated. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 12.")


if __name__ == "__main__":

    main()
