from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

app = FastAPI(
    title="Vietnam Address Converter API",
    description="API for converting Vietnamese addresses between old and new administrative divisions",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, settings.PRODUCTION_FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Server is running"}

@app.get("/")
async def root():
    return {"message": "Vietnam Address Converter API"}

from routers import convert
app.include_router(convert.router)
