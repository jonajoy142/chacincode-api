'''
database connectivity file - Don't change anything this file
'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DatabaseError
from fastapi import Depends
from app.db.env_read import read_env_variables

env_vars = read_env_variables()
host = env_vars['host']
user = env_vars['user']
password = env_vars['password']
database = env_vars['db']


# database connection url
DB_URL = DB_URL = #DB_URL = f"postgresql://{user}:{password}@{host}/{database}"

# create db engine
engine = create_engine(url=DB_URL, pool_size=10)

# session maker of db connection
local_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# base
db_base = declarative_base()


# Dependency to get the database session
def get_db():
    database = local_session()
    try:
        yield database
    finally:
        database.close()


# Check db connection
def check_db_connection(db_session: Session = Depends(get_db)) -> bool:
    """
    check : can connected to database via passed session of database or not
    :param db_session: session of database(instance)
    :return: True(on can connect) or False(can't connect)
    """
    try:
        db_session.execute(text("SELECT 1"))
        return True
    except DatabaseError as db_error:
        print(db_error)
        return False
