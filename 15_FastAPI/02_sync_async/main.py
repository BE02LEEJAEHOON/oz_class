from fastapi import FastAPI
from books import router as books_router
from sync_async_test import router as sync_async_test_router

app = FastAPI()
app.include_router(books_router)
app.include_router(sync_async_test_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', port=8000, log_level='debug', reload=True)