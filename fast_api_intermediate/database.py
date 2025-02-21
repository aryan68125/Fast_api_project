from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHAMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"

connect_args = {"check_same_thread": False}

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()