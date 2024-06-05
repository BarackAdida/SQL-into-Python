from config import conn, cursor

class Student:
    def __init__(self, id, first_name, last_name, gender, age, phone, username, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.phone = phone
        username.phone = username
        self.email = email

    # class method responsible for creating a database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE students(
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            phone INTEGER,
            username TEXT NOT NULL
            email TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    def __repr__(self):
        return f"<Sudent {self.first_name} {self.last_name}>"
    
student = Student(
    1,
    'Adida',
    'Barack',
    18,
    'Male',
    '0110859228',
    'barackadida'
    'barackadida@gmail.com'
)