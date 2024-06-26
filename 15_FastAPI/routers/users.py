from fastapi import APIRouter, Depends, HTTPException
import crud_orm
import dependencies
import schemas
from sqlalchemy.orm import Session
from typing import Union

router = APIRouter()

@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    db_user = crud_orm.create_user(db, user)
    return db_user

# api/v1/users/{user_id}
@router.get('/{user_data}')
def get_user(user_data: Union[int, str], db: Session = Depends(dependencies.get_db)):
    print(f'type: {user_data}')
    print(f'type: {type(user_data)}')

    try: 
        user_data = int(user_data)
        if isinstance(user_data, int):
            db_user = crud_orm.get_user_id(db, user_data)
    except:     
        if isinstance(user_data, str):
            db_user = crud_orm.get_user_email(db, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return db_user

# api/v1/users/email/{user_email}
# @router.get('/email/{user_email}')
# def get_user_email(user_email: str, db: Session = Depends(dependencies.get_db)):
#     db_user = crud.get_user_email(db, user_email)

#     if db_user is None:
#         raise HTTPException(status_code=404, detail='User Not Found')
#     return db_user
    

# api/v1/users/
@router.get('/')
def get_users(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud_orm.get_users(db, skip, limit)

@router.put('/{user_id}')
def update_user(user_id:int, user: schemas.UserUpdate, db: Session = Depends(dependencies.get_db)):
    updated_user = crud_orm.update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return updated_user

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    deleted_user = crud_orm.delete_user(db, user_id)
    
    if delete_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return deleted_user