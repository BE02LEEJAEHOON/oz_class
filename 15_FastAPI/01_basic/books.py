from fastapi import FastAPI, APIRouter

# 로컬 메모리 DB
BOOKS = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "url": "https://example.com/1984",
    }
]

app = FastAPI()
router = APIRouter()

# 루트 페이지
@router.get('/', status_code=200)
def main():
    return {'message': 'Welcome to the Book World! ha ha ha!!'} # 템플릿 코드

# 전체 책 데이터 조회
@router.get('/api/v1/books', status_code=200)
def get_all_books() -> list:
    return BOOKS


# 특정 책 데이터 조회
@router.get('/api/v1/books/{book_id}', status_code=200)
def get_book(book_id: int):
    
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         book
    #         break
    if book:
        return book
    return {'error': 'Book not found, ID: {book_id}'}

# 책 생성
@router.post('/api/v1/books/')
def create_book(book: dict):
    BOOKS.append(book)
    return book

# 책 수정
@router.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book_update: dict):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    
    for key, value in book_update.items():
        if key in book:
            book[key] = value      
    return book
    
# 책 삭제
@router.delete('api/v1/books/{book_id}')
def delete_book(book_id: int):
    global BOOKS
    BOOKS = [item for item in BOOKS if item['id'] != book_id]
    
    return {'message': f'Successfully deleted book with ID: {book_id}'}
    
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('books:app', port=8001, reload=True)