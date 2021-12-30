from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Info(BaseModel):
    name: str
    email: str
    message: str

@app.post("/test")
def test(info: Info):
    print(info.name)
    print(info.message)
    print(info.email)
    return {
        "status": 200,
        "data": {"name": info.name, "email": info.email, "message": info.message}
    }
