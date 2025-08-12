import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)



# uvicorn is used with FastAPI to run the application
# To run this application, use the command: uvicorn main(file name):app(name of the FastAPI onject) --reload (reload will reload the file on changes)

app = FastAPI()
origins = [] # List of origins that are allowed to make requests to this API if * allowed from any where , list of specific URL otherwise
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")  # @app is decorator which maps the root URL to the function below
def hello_fast_api():
    return {"start": "Hello FastAPI application!"}


