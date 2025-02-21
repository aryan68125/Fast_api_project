from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

'''
SQL ALCHEMY ORM HANDLER FILE 
function :
 - To hendle all the query 
 - To handle all the database operations 
'''

connection_string = f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_IP')}/{config('DB_NAME')}"
print(f"Database : Connection string {connection_string}")

db_engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def db_flush():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()