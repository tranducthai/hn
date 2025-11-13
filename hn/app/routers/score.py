from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.services.get_job_predict import get_job_predict_service
from app.models.score import Score

router = APIRouter()

@router.get("/predict", response_model=str, summary="Get job predict")
async def get_job_predict(id: List[float] = Query(..., description="Mảng 8 số")):
    """
    Nhận mảng 8 số qua query param id, trả về 'builder'
    """
    if len(id) != 8:
        raise HTTPException(status_code=422, detail="Bạn phải truyền đúng 8 số")

    # Tạo instance Score từ query param
    score_instance = Score(id=id)
    result = get_job_predict_service.get_job_predict(score_instance)
    return result
