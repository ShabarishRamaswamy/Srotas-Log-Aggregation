from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import src.router

app = FastAPI()

app.include_router(src.router.Router)
app.mount("/", StaticFiles(directory="frontend-build", html = True), name="site")