from models.__init__ import CURSOR, CONN 
from models.school import School
from models.course import Course
from models.student import Student

def initialize_database():
    CURSOR.execute('PRAGMA foreign_keys = ON')  # Enable foreign key constraints
    CONN.commit()

    # Drop existing tables
    Student.drop_table()
    Course.drop_table()
    School.drop_table()

    # Create new tables
    School.create_table()
    Course.create_table()
    Student.create_table()

    # Add some initial records
    add_initial_records()

def add_initial_records():
    # Add schools
    school1 = School.create("St. Patrick's Academy", "Nanyuki")
    school2 = School.create("Chestar High School", "Lamu")
    school3 = School.create("St.Peter's Academy", "Nyeri")
    school4 = School.create("Highland High School", "Nairobi")
    school5 = School.create("Harmony Academy", "Mombasa")
    school6 = School.create("Meru High School", "Kisumu")
    school7 = School.create("Sunrise School", "Eldoret")
    
    

    # Add courses
    course1 = Course.create("Math 101", "Basic Mathematics", school1.id)   # Assigning mulitiple courses to school1
    course2 = Course.create("Science 101", "Basic Science", school1.id)     # Assigning mulitiple courses to school1
    course3 = Course.create("History 101", "Introduction to World History", school2.id)
    course4 = Course.create("Art 101", "Introduction to Art", school2.id)    # Assigning mulitiple courses to school2
    course5 = Course.create("Music 101", "Introduction to Music", school2.id)
    course6 = Course.create("Physics 101", "Basic Physics", school3.id)
    course7 = Course.create("Chemistry 101", "Basic Chemistry", school4.id)
    course8 = Course.create("Biology 101", "Basic Biology", school5.id)   # Assigning multiple courses to school5
    course9 = Course.create("Geography 101", "Basic Geography", school5.id)
    course10 = Course.create("Literature 101", "Introduction to Literature", school6.id)  
    course11 = Course.create("Computer Science 101", "Introduction to Computer Science", school6.id)  # Assigning multiple courses to school6
    course12 = Course.create("Programming 101", "Introduction to Programming", school7.id)

    # Add students
    student1 = Student.create("Nick Roberts", course1.id)
    student2 = Student.create("Zack Kim", course1.id)  # Assigning multiple students to course1
    student3 = Student.create("John Peters", course1.id)  # Assigning multiple students to course1
    student4 = Student.create("Ann Stella", course2.id)
    student5 = Student.create("Abby Duke", course2.id)  # Assigning multiple students to course2
    student6 = Student.create("Charity Johnson", course3.id)
    student7 = Student.create("Brown Blacky", course3.id)  # Assigning multiple students to course3
    student8 = Student.create("Trisha Becky", course4.id)
    student9 = Student.create("Tyler Perry", course5.id)
    student10 = Student.create("William Ruto", course5.id)  # Assigning multiple students to course5
    student11 = Student.create("Brian Musa", course6.id)
    student12 = Student.create("Faith Joy", course6.id)  # Assigning multiple students to course6
    student13 = Student.create("Daniel Meshack ", course7.id)
    student14 = Student.create("Josephine Janet", course7.id)  # Assigning multiple students to course7
    student15 = Student.create("Henry James", course8.id) 
    student16 = Student.create("Joshua Jones", course9.id)  # Assigning multiple students to course9
    student17 = Student.create("Mary Ann", course9.id)
    student18 = Student.create("Chris Brown", course10.id)
    student19 = Student.create("Jennifer Lopez", course11.id)  
    student20 = Student.create("Tory Blacks", course12.id)  
    
# Initialize database when this module is imported
initialize_database()
