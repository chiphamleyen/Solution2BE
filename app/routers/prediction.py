from fastapi import APIRouter, Depends, UploadFile, File

from app.dto.common import BasePaginationResponseData
from app.services.prediction_services import PredictionService
from app.helpers.auth_helpers import get_current_user

router = APIRouter(tags=['Prediction'], prefix="/prediction")

@router.post(
    "/file_upload",
    response_model=BasePaginationResponseData,
)
async def file_upload(
    file: UploadFile = File(...),
    current_user: str = Depends(get_current_user),
):
    file_size = await file.read()
    await file.close()
    if len(file_size) > 10_000_000: # 10MB limit
        return BasePaginationResponseData(
            message="File size exceeds 10MB limit",
            error_code=400
        )
    user_id, role = current_user
    prediction_data = await PredictionService.get_prediction(file_size, user_id, role)
    return BasePaginationResponseData(
        items=prediction_data,
        total=len(prediction_data),
        page=1,
        size=len(prediction_data),
    )