from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

# 동기용 데이터 베이스 접속 명령어 (pymysql 사용)
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:0000@localhost/oz_fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 접속 명령어 (aiomysql 사용)
# 무거운 I/O(5초) 요청이 먼저 들어와도, 뒤에 가벼운 I/O(1초) 요청이 들어오면 더 빨리 끝나는 녀석이 응답한다.
ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:0000@localhost/oz_fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()
