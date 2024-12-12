from database_handler.sql_alchemy_db_handler import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text,Boolean

class posts_sql_alchemy_table(Base):
    __tablename__ = "posts_sql_alchemy_table"
    #define all of the columns
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer,nullable=False,default=0)
    is_published = Column(Boolean, nullable=False, default=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False,default=datetime.now)
