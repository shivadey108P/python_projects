from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    
    aadhar_number = Column("Aadhar Number", Integer, primary_key=True, nullable=False)
    first_name = Column("First Name", String, nullable=False)
    last_name = Column("Last Name", String, nullable=False)
    gender = Column("Gender", CHAR, nullable=False)
    age = Column("Age", Integer, nullable=False)
    
    def __init__(self, aadhar_number, first_name, last_name, gender, age):
        self.aadhar_number = aadhar_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        
    def __representation__(self):
        return f"| {self.aadhar_number} | {self.first_name} | {self.last_name} | {self.gender} | {self.age} |"
    
engine = create_engine("sqlite:///./day-63/sql_alchemy_practice/my_db.db", echo=True)
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind=engine)
session = Session()

# p1 = Person(123456789, "Mike", "Smith", "M", 27)

# session.add(p1)

# session.commit()

# p2 = Person(453422443, "Angela", "Lui", "F", 22)
# p3 = Person(543245344, "Cristina", "Blue", "F", 37)
# p4 = Person(345666432, "Kyle", "Blue", "M", 43)

# session.add(p2)
# session.add(p3)
# session.add(p4)

# session.commit()

results = session.query(Person).filter(Person.first_name.in_(['Angela', 'Mike']))
for r in results:
    print(r.aadhar_number, r.first_name, r.last_name, r.gender, r.age)