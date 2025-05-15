from pydantic import BaseModel, Field

class FeedbackRequest(BaseModel):
    content: str

class FeedbackResponseData(BaseModel):
    PydanticObjectId = Field(alias='_id')
    content: str
    created_at: str
    updated_at: str
    user_id: str

