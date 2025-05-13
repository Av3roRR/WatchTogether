from fastapi import FastAPI

from app.users.router import router as users_router

app = FastAPI(title="Watch Together")

app.include_router(users_router)