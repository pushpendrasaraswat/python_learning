from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils
from ..utils import verify_password
from ..oauth2 import create_access_token


router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(database.get_db)):
    user_in_db = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    print(user_in_db.id)
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    if not verify_password(user_credentials.password, user_in_db.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    #create a token
    access_token = create_access_token(data={"user_id":user_in_db.id})

    return {"access_token": access_token, "token_type": "bearer"}




