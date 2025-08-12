from fastapi import  Depends, HTTPException, status, Response, APIRouter
from .. import models,schemas,oauth2
from ..database import  get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts", tags=["Posts"]) # This prefix will be added to all the endpoints in this router like @restMapping at controller level in java

@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0):
    print(current_user.email)
    print(limit)
    print(skip)
    # get all posts for the current user
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    # get post with pagination
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).limit(limit).offset(skip).all()
    # db_cursor.execute("SELECT * FROM posts")
    # posts = db_cursor.fetchall()
    return posts


@router.get("/{post_id}", response_model=schemas.PostResponse) # This endpoint creates a post with a specific ID path parameter
def get_post_for_id(post_id : int, response: Response, db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    #db_cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
    #post = db_cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with {post_id} not found")
    return post
    #else:
        # This is one way of handling 404 Not Found error ,
        # other is raise an Exception
        # response.status_code = status.HTTP_404_NOT_FOUND

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    #db_cursor.execute("DELETE FROM posts WHERE id = %s returning *", (post_id,))
    #deleted_post = db_cursor.fetchone()
    #db_connection.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == post_id)
    print(f"Deleted post with id {post_id}, {deleted_post}")
    if deleted_post.first() is None:
        raise HTTPException(status_code=404, detail=f"Post with {post_id} not found")
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    deleted_post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{post_id}",  response_model=schemas.PostResponse)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
   # db_cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s returning *",
    #                 (post.title, post.content, post.published, post_id))
    #update_post = db_cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    first_post = post_query.first()
    if first_post is None:
        raise HTTPException(status_code=404, detail=f"Post with {post_id} not found")

    if first_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail="Not authorized to perform requested action")
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    #db_connection.commit()
    return  post_query.first()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)  # This endpoint creates a new post
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    print(post.model_dump())
    #new_post = models.Post(title=post.title, content=post.content,rating=post.rating)
    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

