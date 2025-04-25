from sqlmodel import Session, SQLModel
from db.dbConn import engine

async def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield