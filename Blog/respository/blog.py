from fastapi import Depends, status, HTTPException
from ..database import get_db
from .. import dlschemas, models
from typing import List
from sqlalchemy.orm import Session


def show(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create(blogss:dlschemas.Blog, db: Session):
    new_blog = models.Blog(title=blogss.title, body=blogss.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id:int, blog : dlschemas.Blog, db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).update(blog.dict(), synchronize_session=False)
    db.commit()
    return {"message" : f"Successfuully Update ID {id}"}

def get_id(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Blog with the ID of {id} not found") 
    return blog
    
def delete_blog(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)#.delete(synchronize_session=False)
    
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog with the ID {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'message' : " Blog Successfully Deleted"}