from sqlalchemy import create_engine, Integer, String, Float, Column
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine= create_engine('postgres+psycopg2://postgres:postgres@localhost:5432/AssumeItWorks',echo=True)

Base = declarative_base()

class Person(Base):
    __tablename_ = 'people'
    id = Column(Integer,primary_key=True)
    name = Column(String,nullabl=False)
    age= Column(Integer)
    things = relationship('Thing',back_populates='person')  #practicing with the syntax how to make a table for people

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer,primary_key=True)
    description = Column(String,nullabl=False)
    value= Column(Integer)
    owner = Column(Integer, ForeignKey('people.id')) #incorporating foreign keys into tables

    # person = relationship('Person',back_populates='things')

Base.metadata.create_all(engine)

Session= sessionmaker(bind=engine)
session = Session

new_person= Person(name='Sam',age=80)
session.add(new_person)
session.commit()
