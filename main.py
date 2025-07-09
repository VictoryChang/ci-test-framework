from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

from calculator import sum, double_sum


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "Online"}


@app.get("/api/sum")
async def get_api_sum(a: int, b: int) -> dict:
    return {"result": sum(a, b)}


@app.get("/api/double_sum")
async def get_api_sum(a: int, b: int) -> dict:
    return {"result": double_sum(a, b)}


@app.get("/ui/sum", response_class=HTMLResponse)
async def get_ui_sum(a: int, b: int):
    return f'<div id="sum">{sum(a, b)}</div>'


@app.get("/ui/double_sum", response_class=HTMLResponse)
async def get_ui_sum(a: int, b: int):
    return f'<div id="double_sum">{double_sum(a, b)}</div>'



if __name__ == "__main__":
    uvicorn.run(app)
