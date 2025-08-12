from fastapi import  Depends, HTTPException, status, APIRouter
from .. import models,schemas, utils
from ..database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["user"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)  # This endpoint creates a new post
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    hash_password = utils.hash(user.password)
    user.password = hash_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=schemas.UserResponse)  # This endpoint creates a new post
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {user_id} not found")
    return user