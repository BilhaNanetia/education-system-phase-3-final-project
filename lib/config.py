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
    course1 = Course.create("Math 101", "Basic Mathematics", school1.id)
    course2 = Course.create("Science 101", "Basic Science", school2.id)
    course3 = Course.create("History 101", "Introduction to World History", school3.id)
    course4 = Course.create("Art 101", "Introduction to Art", school1.id)
    course5 = Course.create("Music 101", "Introduction to Music", school2.id)
    course6 = Course.create("Physics 101", "Basic Physics", school4.id)
    course7 = Course.create("Chemistry 101", "Basic Chemistry", school5.id)
    course8 = Course.create("Biology 101", "Basic Biology", school6.id)
    course9 = Course.create("Geography 101", "Basic Geography", school7.id)
    course10 = Course.create("Literature 101", "Introduction to Literature", school5.id)

    # Add students
    student1 = Student.create("Alice Johnson", course1.id)
    student2 = Student.create("Bob Smith", course2.id)
    student3 = Student.create("Charlie Brown", course3.id)
    student4 = Student.create("David Wilson", course4.id)
    student5 = Student.create("Emma Davis", course5.id)
    student6 = Student.create("Fiona Clark", course6.id)
    student7 = Student.create("George White", course7.id)
    student8 = Student.create("Hannah Scott", course8.id)
    student9 = Student.create("Ian Taylor", course9.id)
    student10 = Student.create("Julia Roberts", course10.id)

# Initialize database when this module is imported
initialize_database()
