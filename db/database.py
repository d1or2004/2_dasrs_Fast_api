from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:2004@localhost/fast_ip', echo=True)

Base = declarative_base()
session = sessionmaker
