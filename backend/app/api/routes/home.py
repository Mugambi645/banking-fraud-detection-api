from fastapi import APIRouter, FastAPI


router = APIRouter(prefix="/home")

@router.get("/")
def home():
    return {"message": "Welcome to my fastAPI banking app"}