import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import src.router

app = FastAPI()
PORT = 8000

app.include_router(src.router.Router)
app.mount("/", StaticFiles(directory="backend/frontend-build", html = True), name="site")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)