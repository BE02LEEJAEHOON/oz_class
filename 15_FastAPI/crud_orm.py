from models import User, Item
# from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
import bcrypt # pip insall bcrypt
# create user
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    
    return db_user # object -> json (역직렬화)

# user의 id값을 기반으로 데이터를 찾는다.
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 전체 유저를 불러와 봅시다. (페이지 네이션)
def get_users(db: Session, skip: int=0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# 유저 업데이트
def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        return None
    
    user_data = user_update.dict()

    for key, value in user_data.items():
        setattr(db_user, key, value) # setattr : 파이썬 내장함수 (OBJ, Key, Value)

    db.commit()
    db.refresh(db_user)

    return db_user

# 유저 삭제
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None
    
    db.delete(db_user)
    db.commit()
    return db_user