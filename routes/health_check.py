import os

from fastapi.requests import Request
from fastapi import APIRouter
from fastapi import status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def health_check(request: Request):
    return {"status": "Success !"}