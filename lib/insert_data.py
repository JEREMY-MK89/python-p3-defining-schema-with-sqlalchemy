# insert_data.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_sandbox import Base, Student  # Update with the actual name of your main script

# Create an SQLite engine pointing to the database file
engine = create_engine('sqlite:///students.db', echo=True)

# Create a session to interact with the database
session = Session(engine)

# Insert data into the 'students' table
def insert_student_data(name):
    student = Student(name=name)
    session.add(student)
    session.commit()

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Insert sample data (replace 'John Doe' with the desired name)
    insert_student_data('John Doe')

    # You can insert more data by calling insert_student_data multiple times

    # Close the session
    session.close()
