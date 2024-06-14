# lib/models/course.py
from models.__init__ import CURSOR, CONN

class Course:
    """
    Represents a course in the education system.
    """
    all = {}  # Dictionary to store all course instances with their IDs as keys

    def __init__(self, title, description, school_id, id=None):
        """
        Initializes a new Course instance.
        """
        self.id = id
        self.title = title
        self.description = description
        self.school_id = school_id

    def __repr__(self):
        """
        Returns a string representation of the course.
        """
        return f"<Course {self.id}: {self.title}, {self.description}, School ID: {self.school_id}>"

    @property
    def title(self):
        """
        Gets or sets the title of the course.
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Validates and sets the title of the course.
        """
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def description(self):
        """
        Gets or sets the description of the course.
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Validates and sets the description of the course.
        """
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string")

    @property
    def school_id(self):
        """
        Gets or sets the school ID of the course.
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        from models.school import School

        """
        Validates and sets the school ID of the course.
        """
        if isinstance(school_id, int) and School.find_by_id(school_id):
            self._school_id = school_id
        else:
            raise ValueError("school_id must reference a school in the database")

    @classmethod
    def create_table(cls):
        """
        Creates the courses table in the database.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES schools(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drops the courses table in the database.
        """
        sql = "DROP TABLE IF EXISTS courses"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """
        Saves the course to the database.
        """
        sql = "INSERT INTO courses (title, description, school_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.title, self.description, self.school_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self        # Adds the course instance to the all dictionary

    @classmethod
    def create(cls, title, description, school_id):
        """
        Creates a new course and saves it to the database.
        """
        course = cls(title, description, school_id)
        course.save()
        return course

    def update(self):
        """
        Updates the course in the database.
        """
        sql = "UPDATE courses SET title = ?, description = ?, school_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.title, self.description, self.school_id, self.id))
        CONN.commit()

    def delete(self):
        """
        Deletes the course from the database.
        """
        sql = "DELETE FROM courses WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]       # Removes the course instance from the all dictionary
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """
        Creates a Course instance from a database row.
        """
        course = cls.all.get(row[0])     # Check if the course instance already exists
        if course:
            course.title = row[1]
            course.description = row[2]
            course.school_id = row[3]
        else:
            course = cls(row[1], row[2], row[3])
            course.id = row[0]
            cls.all[course.id] = course       # Adds the course instance to the all dictionary
        return course

    @classmethod
    def get_all(cls):
        """
        Returns a list of all courses in the database.
        """
        sql = "SELECT * FROM courses"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """
        Finds a course by ID in the database.
        """
        sql = "SELECT * FROM courses WHERE id =?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """
        Finds a course by title in the database.
        """
        sql = "SELECT * FROM courses WHERE lower(title) = lower(?)"  # Find by title to be case insensitive
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def students(self):
        """
        Returns a list of students enrolled in this course.
        """
        from models.student import Student
        sql = "SELECT * FROM students WHERE course_id =?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Student.instance_from_db(row) for row in rows]