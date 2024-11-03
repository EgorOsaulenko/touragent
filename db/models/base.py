from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///travel_agency.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def create_db():
    Base.metadata.create_all(bind=engine)
