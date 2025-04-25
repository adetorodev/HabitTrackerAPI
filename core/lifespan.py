from fastapi import FastAPI
from dependencies.dbDepends import create_db_and_table, get_session
from contextlib import asynccontextmanager

@asynccontextmanager
async def startup_handler(app: FastAPI):
    await create_db_and_table()
    get_session
    yield
