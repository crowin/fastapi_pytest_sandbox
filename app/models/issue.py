from datetime import datetime

from pydantic import BaseModel


class IssueDto(BaseModel):
    id: str
    created_at: datetime
    author: str
    label: str
    description: str
    priority: int
