# lib/models/student.py
from models.__init__ import CURSOR, CONN

class Student:
    """
    Represents a student in the education system.
    """
    all = {}  # list of all students

    def __init__(self, name, course_id, id=None):
        """
        Initializes a new Student instance.
        """
        self.id = id
        self.name = name
        self.course_id = course_id

    def __repr__(self):
        """
        Returns a string representation of the student.
        """
        return f"<Student {self.id}: {self.name}, Course ID: {self.course_id}>"

    @property
    def name(self):
        """
        Gets or sets the name of the student.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Validates and sets the name of the student.
        """
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def course_id(self):
        """
        Gets or sets the course ID of the student.
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        from models.course import Course

        """
        Validates and sets the course ID of the student.
        """
        if isinstance(course_id, int) and Course.find_by_id(course_id):
            self._course_id = course_id
        else:
            raise ValueError("Course ID must reference a course in the database")

    @classmethod
    def create_table(cls):
        """
        Creates the students table in the database.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drops the students table in the database.
        """
        sql = "DROP TABLE IF EXISTS students"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """
        Saves the student to the database.
        """
        sql = "INSERT INTO students (name, course_id) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.course_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, course_id):
        """
        Creates a new student and saves it to the database.
        """
        student = cls(name, course_id)
        student.save()
        return student

    def update(self):
        """
        Updates the student in the database.
        """
        sql = "UPDATE students SET name = ?, course_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.course_id, self.id))
        CONN.commit()

    def delete(self):
        """
        Deletes the student from the database.
        """
        sql = "DELETE FROM students WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """
        Creates a Student instance from a database row.
        """
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.course_id = row[2]
        else:
            student = cls(row[1], row[2])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        """
        Returns a list of all students in the database.
        """
        sql = "SELECT * FROM students"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """
        Finds a student by ID in the database.
        """
        sql = "SELECT * FROM students WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """
        Finds a student by name in the database.
        """
        sql = "SELECT * FROM students WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None