from fastapi import APIRouter, Depends
from .. import database, schemas
router = APIRouter(
    tags=['Users'],
    prefix='/user'
)
get_db = database.get_db
from sqlalchemy.orm import Session
from ..repository import user






@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id ,db: Session = Depends(get_db)):
    user.show(id,db)
