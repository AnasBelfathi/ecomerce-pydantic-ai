from fastapi import FastAPI

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

# Serve uploaded files statically
from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
