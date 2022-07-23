from fastapi import FastAPI

from src.routes.polls import router as polls_router
from src.routes.auth import router as auth_router
from src.routes.groups import router as groups_router
from src.settings.db import create_sessionmaker


Session = create_sessionmaker()

app = FastAPI()

# Add routers
app.include_router(polls_router)
app.include_router(auth_router)
app.include_router(groups_router)
