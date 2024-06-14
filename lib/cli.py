import sys
from models.school import School
from models.course import Course
from models.student import Student

def exit_program():
    print("Goodbye!")
    sys.exit()

def main_menu():
    while True:
        print("\n*************** MAIN MENU ***************")
        print("1. Manage Schools")
        print("2. Manage Courses")
        print("3. Manage Students")
        print("4. Exit")
        print("*****************************************")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            school_menu()

        elif choice == "2":
            course_menu()

        elif choice == "3":
            student_menu()

        elif choice == "4":
            exit_program()  # Call the exit_program function here

        else:
            print("Invalid choice. Please try again.")

def school_menu():
    while True:
        print("\n*************** SCHOOL MENU ***************")
        print("1. Add School")
        print("2. Update School")
        print("3. Delete School")
        print("4. View All Schools")
        print("5. Find School by Name")
        print("6. Find School by ID")
        print("7. Return to Main Menu")
        print("*******************************************")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter school name: ")
            location = input("Enter school location: ")
            School.create(name, location)
            print("School added successfully.")

        elif choice == "2":
            id = input("Enter school ID to update: ")
            school = School.find_by_id(int(id))
            if school:
                new_name = input("Enter new name: ")
                new_location = input("Enter new location: ")
                school.name = new_name
                school.location = new_location
                school.update()
                print("School updated successfully.")
            else:
                print(f"School with ID {id} not found.")

        elif choice == "3":
            id = input("Enter school ID to delete: ")
            school = School.find_by_id(int(id))
            if school:
                school.delete()
                print("School deleted successfully.")
            else:
                print(f"School with ID {id} not found.")

        elif choice == "4":
            schools = School.get_all()
            for school in schools:
                print(school)

        elif choice == "5":
            name = input("Enter school name to find: ")
            school = School.find_by_name(name)
            if school:
                print(school)
            else:
                print(f"School with name '{name}' not found.")

        elif choice == "6":
            id = input("Enter school ID to find: ")
            school = School.find_by_id(int(id))
            if school:
                print(school)
            else:
                print(f"School with ID {id} not found.")

        elif choice == "7":
            return

        else:
            print("Invalid choice. Please try again.")

def course_menu():
    while True:
        print("\n*************** COURSE MENU ***************")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. View All Courses")
        print("5. Find Course by Title")
        print("6. Find Course by ID")
        print("7. Return to Main Menu")
        print("*******************************************")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter course title: ")
            description = input("Enter course description: ")
            school_id = input("Enter school ID: ")
            Course.create(title, description, int(school_id))
            print("Course added successfully.")

        elif choice == "2":
            id = input("Enter course ID to update: ")
            course = Course.find_by_id(int(id))
            if course:
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                new_school_id = input("Enter new school ID: ")
                course.title = new_title
                course.description = new_description
                course.school_id = int(new_school_id)
                course.update()
                print("Course updated successfully.")
            else:
                print(f"Course with ID {id} not found.")

        elif choice == "3":
            id = input("Enter course ID to delete: ")
            course = Course.find_by_id(int(id))
            if course:
                course.delete()
                print("Course deleted successfully.")
            else:
                print(f"Course with ID {id} not found.")

        elif choice == "4":
            courses = Course.get_all()
            for course in courses:
                print(course)

        elif choice == "5":
            title = input("Enter course title to find: ")
            course = Course.find_by_title(title)
            if course:
                print(course)
            else:
                print(f"Course with title '{title}' not found.")

        elif choice == "6":
            id = input("Enter course ID to find: ")
            course = Course.find_by_id(int(id))
            if course:
                print(course)
            else:
                print(f"Course with ID {id} not found.")

        elif choice == "7":
            return

        else:
            print("Invalid choice. Please try again.")

def student_menu():
    while True:
        print("\n*************** STUDENT MENU ***************")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Find Student by Name")
        print("6. Find Student by ID")
        print("7. Return to Main Menu")
        print("*******************************************")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            course_id = input("Enter course ID: ")
            Student.create(name, int(course_id))
            print("Student added successfully.")

        elif choice == "2":
            id = input("Enter student ID to update: ")
            student = Student.find_by_id(int(id))
            if student:
                new_name = input("Enter new name: ")
                student.name = new_name
                new_course_id = input("Enter new course ID: ")
                student.course_id = int(new_course_id)
                student.update()
                print("Student updated successfully.")
            else:
                print(f"Student with ID {id} not found.")

        elif choice == "3":
            id = input("Enter student ID to delete: ")
            student = Student.find_by_id(int(id))
            if student:
                student.delete()
                print("Student deleted successfully.")
            else:
                print(f"Student with ID {id} not found.")

        elif choice == "4":
            students = Student.get_all()
            for student in students:
                print(student)

        elif choice == "5":
            name = input("Enter student name to find: ")
            student = Student.find_by_name(name)
            if student:
                print(student)
            else:
                print(f"Student with name '{name}' not found.")

        elif choice == "6":
            id = input("Enter student ID to find: ")
            student = Student.find_by_id(int(id))
            if student:
                print(student)
            else:
                print(f"Student with ID {id} not found.")

        elif choice == "7":
            return

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
