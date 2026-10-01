from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import pyodbc

db_url = (
    "mssql+pyodbc://@DESKTOP-GI1T9TB\\SQLEXPRESS/task_db"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

print("Db Connected !")

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)







































# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker , declarative_base

# DATABASE_URL="sqlite:///./tasks.db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread":False}
# )

# SessionLocal = sessionmaker(
#     autocommit = False,
#     autoflush = False,
#     bind=engine
# )

# Base = declarative_base()

# def get_db():
#     db= SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()