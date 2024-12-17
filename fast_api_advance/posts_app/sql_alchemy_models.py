from database_handler.sql_alchemy_db_handler import Base
from sqlalchemy import Column, Integer, String, DateTime, Text,Boolean, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.schema import FetchedValue

class posts_sql_alchemy_table(Base):
    __tablename__ = "posts_sql_alchemy_table"
    #define all of the columns
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False, default=0, server_default="0")  # Add server_default
    is_published = Column(Boolean, nullable=False, default=True, server_default="true")  # Add server_default
    is_deleted = Column(Boolean, nullable=False, default=False, server_default="false")  # Add server_default
    created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())  # Add server_default
    # created_by = Column(Integer, ForeignKey('UserMaster.id', ondelete='CASCADE'), nullable=False)

class UserMaster(Base):
    __tablename__ = "user_master"
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String,nullable=False, unique=True)
    password = Column(String,nullable=False,)
    is_deleted = Column(Boolean,nullable=False,server_default="false")
    is_blocked = Column(Boolean,nullable=False,server_default="true")
    verify_otp = Column(Boolean,nullable=False,server_default="false")
    created_at = Column(DateTime,nullable=False,default = func.now(), server_default=func.now())
    account_activation_otp = Column(Integer, nullable=True, server_default=text("0"))


