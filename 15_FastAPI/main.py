from fastapi import FastAPI
from sockets import router
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_html = Path("index.html").read_text()
    return HTMLResponse(content=index_html)

# uvicorn main:app --reload