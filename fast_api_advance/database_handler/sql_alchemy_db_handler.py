from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"
connection_string = f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_IP')}/{config('DB_NAME')}"
print(connection_string)
db_engine  = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=db_engine)

Base = declarative_base()