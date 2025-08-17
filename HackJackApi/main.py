from fastapi import FastAPI
from app.routes import gameplay
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HackJack API",
    description="Documentation for HackJack API functionality",
    version="0.0.1"
)

origins = [
    "http://localhost:4200",
    "http://localhost:4201"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/heartbeat", tags=["Health"])
async def health():
    return {"message": "HackJack dealer is online"}

app.include_router(gameplay.router)
