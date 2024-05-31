from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

from .chains import get_translation_chain

# Create FastAPI app
app = FastAPI(
    title="LangChain Server",
    description="API for LangChain's Runnable interfaces",
    version="1.0",
)


# Redirect root to docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


# Add chain route
add_routes(app, get_translation_chain(), path="/translate")
