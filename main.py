from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.routes import products, orders, cart, chatbot
import os
import uvicorn
import logfire

# Initialize FastAPI app
app = FastAPI()

# Configure Logfire for Observability
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_fastapi(app)
logfire.instrument_pydantic()

# Create uploads folder for product images
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Include API route modules
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(cart.router)
app.include_router(chatbot.router)

# Serve uploaded images statically
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Serve frontend JS/CSS assets at /src (matches <script src="/src/main.js">)
app.mount("/src", StaticFiles(directory="frontend/src"), name="frontend-src")

# Serve index.html at root
@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
