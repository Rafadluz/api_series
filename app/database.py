from sqlalchemy import create_engine, text
from sqlalchemy.orm import  sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

SERVER_URL = "mysql+pymysql://root:admin@localhost"

engine_server = create_engine(SERVER_URL)

with engine_server.connect()as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS series_api"))
    conn.commit

#DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()