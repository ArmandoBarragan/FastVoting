from fastapi import FastAPI

from src.polls.routes import router as polls_router


app = FastAPI()

app.include_router(polls_router)