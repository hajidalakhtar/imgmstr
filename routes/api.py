from fastapi import APIRouter
from src.endpoints import  image

router = APIRouter()
router.include_router(image.router)