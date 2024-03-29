
from fastapi import    FastAPI

from httpx import post
from passlib.context import CryptContext
app = FastAPI()
from . import models
from .database import engine
from .routers import oauth, post, users

# pwd_context= CryptContext(schemes=["bcrypt"], deprecated=" auto")
models.Base.metadata.create_all(bind=engine)



app.include_router(post.router)
app.include_router(users.router)
app.include_router(oauth.router)


@app.get("/")
def root():
    return {"message": "welcome to my api!"}







