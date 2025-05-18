from datetime import datetime
from beanie import PydanticObjectId
from pydantic import BaseModel, Field

class FeedbackRequest(BaseModel):
    content: str

class FeedbackResponseData(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    content: str
    created_at: datetime
    updated_at: datetime
    user_id: str

