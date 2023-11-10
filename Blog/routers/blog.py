from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import dlschemas, models, database, O2auth
from typing import List
from sqlalchemy.orm import Session, relationship
from ..respository import blog

get_db = database.get_db
router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)


@router.get('/', response_model=List[dlschemas.ShowBlog])
def show(db: Session = Depends(database.get_db), current_user:dlschemas.User = Depends(O2auth.get_current_user)):
    return blog.show(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blogss: dlschemas.Blog, db: Session= Depends(get_db), current_user:dlschemas.User = Depends(O2auth.get_current_user)):
    return blog.create(blogss, db)

@router.get('/{id}', response_model=dlschemas.ShowBlog)
def get_by_id(id: int, response:Response, db: Session= Depends(get_db), current_user:dlschemas.User = Depends(O2auth.get_current_user)):
    return blog.get_id(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blogss : dlschemas.Blog, db : Session = Depends(get_db), current_user:dlschemas.User = Depends(O2auth.get_current_user)):
    return blog.update(id,blogss, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db), current_user:dlschemas.User = Depends(O2auth.get_current_user)):
    return blog.delete_blog(id, db)