from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, oauth2
from ..repository import blog

from sqlalchemy.orm import Session

router=APIRouter(
    tags=['Blog'],  
    prefix='/blog'

)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog.create(request, db)
    

@router.get('/{id}', status_code = 200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show_one(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request,db)



@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
