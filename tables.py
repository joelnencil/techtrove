from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define your model before calling create_all
class UserDetails(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

# PostgreSQL database connection Configuration
DATABASE_URL = f"postgresql://postgres:Jojima2003@localhost:5001/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the table
Base.metadata.create_all(bind=engine)
