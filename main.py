from fastapi import FastAPI
from core.lifespan import startup_handler

app = FastAPI(lifespan=startup_handler)

# @app.on_event("startup")
# def on_startup():
#     create_db_and_table()