from fastapi import APIRouter, FastAPI
from app.core.logging import get_logger


logger = get_logger()
router = APIRouter(prefix="/home")

@router.get("/")
def home():
    logger.info("Home endpoint called")
    logger.debug("Home endpoint called")
    logger.error("Home endpoint called")
    logger.warning("Home endpoint called")
    logger.critical("Home endpoint called")
    return {"message": "Welcome to my fastAPI banking app"}