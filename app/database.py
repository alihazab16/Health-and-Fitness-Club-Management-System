import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL) #should be made a configured environ variable
                                     #using PostgreSQL connection like 
                                     # postgresql+psycopg://username:password@localhost:5432/database_name

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass