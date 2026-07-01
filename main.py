from contextlib import asynccontextmanager
from router import router as tasks_router
from database import create_tables, delete_tables
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Db is cleaned")
    await create_tables()
    print("Application startup...")
    yield
    print("Application shutdown...")


app = FastAPI(lifespan=lifespan)


app.include_router(tasks_router)
