from pymongo import ASCENDING, IndexModel

from app.models.base import RootModel, RootEnum
from app.models.user import UserRoleEnum

class History(RootModel):
    class Settings:
        name = "history"
        indexes = [
            IndexModel(
                [
                    ("submitter_id", ASCENDING),
                ]
            )
        ]
    submitter_id: str #ID of the submitter
    submitter_role: UserRoleEnum
    timestamp: str
    detection: bool
    severity: float