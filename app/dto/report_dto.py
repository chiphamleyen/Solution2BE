from datetime import datetime
from typing import List
from pydantic import BaseModel
from app.dto.common import BaseResponseData

class HistoryResponseData(BaseModel):
    timestamp: str
    detection: bool
    classifier: str
    severity: float
    created_at: datetime

class ClassifierResponseData(BaseModel):
    type: str
    total: int

class ReportResponseData(BaseModel):
    detection_benign: int = 0
    detection_malware: int = 0
    classifier: List[ClassifierResponseData] = []
    mean_severity: float = 0.0

class ReportResponse(BaseResponseData):
    data: ReportResponseData