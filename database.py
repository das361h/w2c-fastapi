from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql://root:GEyrFPejWzghAJcnaDPJMiaHqVjIxVsD@mysql.railway.internal:3306/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
