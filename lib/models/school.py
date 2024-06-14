# lib/models/school.py
from models.__init__ import CURSOR, CONN

class School:
    """
    Represents a school in the education system.
    """
    all = {}  # Dictionary to store all school instances  with their IDs as keys

    def __init__(self, name, location, id=None):
        """
        Initializes a new School instance.
        """
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        """
        Returns a string representation of the school.
        """
        return f"<School {self.id}: {self.name}, {self.location}>"

    @property
    def name(self):
        """
        Gets or sets the name of the school.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Validates and sets the name of the school.
        """
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def location(self):
        """
        Gets or sets the location of the school.
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Validates and sets the location of the school.
        """
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")

    @classmethod
    def create_table(cls):
        """
        Creates the schools table in the database.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drops the schools table in the database.
        """
        sql = "DROP TABLE IF EXISTS schools"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """
        Saves the school to the database.
        """
        sql = "INSERT INTO schools (name, location) VALUES (?, ?)"
        try:
            CURSOR.execute(sql, (self.name, self.location))
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self  # Adds the school instance to the all dictionary
        except Exception as e:
            CONN.rollback()
            raise e

    @classmethod
    def create(cls, name, location):
        """
        Creates a new school and saves it to the database.
        """
        school = cls(name, location)
        school.save()
        return school

    def update(self):
        """
        Updates the school in the database.
        """
        sql = "UPDATE schools SET name = ?, location = ? WHERE id = ?"
        try:
            CURSOR.execute(sql, (self.name, self.location, self.id))
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            raise e

    def delete(self):
        """
        Deletes the school from the database.
        """
        sql = "DELETE FROM schools WHERE id = ?"
        try:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            del type(self).all[self.id]  # Removes the school instance from the all dictionary
            self.id = None    # Sets the instance's id to None
        except Exception as e:
            CONN.rollback()
            raise e

    @classmethod
    def instance_from_db(cls, row):
        """
        Creates a School instance from a database row.
        """
        try:
            school = cls.all.get(row[0])    # Check if the school instance already exists
            if school:
                school.name = row[1]
                school.location = row[2]
            else:
                school = cls(row[1], row[2])
                school.id = row[0]
                cls.all[school.id] = school   # Adds the school instance to the all dictionary
            return school
        except Exception as e:
            raise ValueError(f"Invalid data in row: {row}")

    @classmethod
    def get_all(cls):
        """
        Returns a list of all schools in the database.
        """
        sql = "SELECT * FROM schools"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """
        Finds a school by ID in the database.
        """
        sql = "SELECT * FROM schools WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """
        Finds a school by name in the database.
        """
        sql = "SELECT * FROM schools WHERE lower(name) = lower(?)"   # Find by name to be case insensitive
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def courses(self):
        """
        Returns a list of courses for this school.
        """
        from models.course import Course
        sql = "SELECT * FROM courses WHERE school_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Course.instance_from_db(row) for row in rows]