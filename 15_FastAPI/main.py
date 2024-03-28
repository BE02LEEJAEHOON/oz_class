from fastapi import FastAPI

app = FastAPI()

# Router
@app.get('/')
def read_root():
    return {'Hello': 'World'}


if __name__ == '__main__':
    # ASGI 서버
    import uvicorn
    uvicorn.run('main:app', port=8000, log_level='debug', reload=True)