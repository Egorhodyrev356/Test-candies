from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base = declarative_base()
class Candies(Base):
    __tablename__ = 'candies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    appearance = Column(Integer)
    fragility = Column(Integer)
    density = Column(Integer)
    taste_fill = Column(Integer)
    taste_glaze = Column(Integer)
    crispy = Column(Integer)
    final_mark = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



