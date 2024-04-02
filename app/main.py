
from fastapi import    FastAPI
from fastapi.middleware.cors import CORSMiddleware
from httpx import post
from passlib.context import CryptContext
app = FastAPI()
from . import models
from .database import engine
from .routers import oauth, post, users, vote
from .config import settings


# print(settings.database_username)
# pwd_context= CryptContext(schemes=["bcrypt"], deprecated=" auto")
             
# models.Base.metadata.create_all(bind=engine)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(users.router)
app.include_router(oauth.router)
app.include_router(vote .router)


@app.get("/")
def root():
    return {"message": "hllo aaa"}







