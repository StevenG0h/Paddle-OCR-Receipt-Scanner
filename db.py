import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, TIMESTAMP

engine = create_engine(
    'mysql+mysqlconnector://atong:password@localhost:3306/receipt',
    echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    subtotal = Column(Integer)
    tax      = Column(Integer)
    total    = Column(Integer)
    created_at = Column(TIMESTAMP, 
                        default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)