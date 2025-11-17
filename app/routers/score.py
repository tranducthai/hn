from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.services.get_job_predict import get_job_predict_service
from app.models.score import Score

router = APIRouter()

@router.post("/predict", response_model=str, summary="Get job predict")
async def get_job_predict(score: Score):
    """
    Nhận body JSON:
    {
        "id": [1,2,3,4,5,6,7,8]
    }
    """
    if len(score.id) != 8:
        raise HTTPException(status_code=422, detail="Bạn phải truyền đúng 8 số")

    result = get_job_predict_service.get_job_predict(score)
    return result