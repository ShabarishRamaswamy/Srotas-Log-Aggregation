# backend/main.py
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

# --- API Routes ---
# Your API logic goes here.
@app.get("/api/hello")
async def hello():
    """A simple endpoint to confirm the API is running."""
    return {"message": "Hello from the Srotas Backend! 👋"}


# --- Static Files and Frontend ---
# This MUST come AFTER your API routes.

# 1. Mount the 'static' folder from React's build output
# The path to the static directory, which contains CSS, JS, etc.
# Note: The 'name' must be "static" for this to work with React's build
static_files_dir = os.path.join(os.path.dirname(__file__), "frontend-build/static")
app.mount("/static", StaticFiles(directory=static_files_dir), name="static")

# 2. A catch-all route to serve the index.html
# This is for client-side routing. Any path not matching an API route
# will be served the main React app file.
@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_path = os.path.join(os.path.dirname(__file__), "static/index.html")
    if not os.path.exists(index_path):
        return {"error": "index.html not found"}, 404
    return FileResponse(index_path)