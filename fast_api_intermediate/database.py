from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)