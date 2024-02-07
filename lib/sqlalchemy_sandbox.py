#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Step 1: Define the base class for declarative syntax
Base = declarative_base()

# Step 2: Define the data model class for the 'students' table
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Step 3: Create an SQLite engine pointing to the database file
engine = create_engine('sqlite:///students.db', echo=True)

# Step 4: Check if the script is being run as the main program
if __name__ == '__main__':
    # Step 5: Create tables based on the defined models
    Base.metadata.create_all(engine)
