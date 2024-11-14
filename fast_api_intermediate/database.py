from sqlalchemy import create_engine

SQLALCHAMY_DATABASE_URL = "sqlite+pysqlite:///./blog.db"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)