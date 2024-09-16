from typing import List, Annotated
from fastapi import APIRouter, Depends

from app.auth.api_key_auth import api_key_auth
from app.models.issue import IssueDto
from app.mock import mock_data
from app.models.user import UserDto

router = APIRouter(prefix="/issues")

@router.get("/{issue_id}", response_model=IssueDto)
async def get_issue(issue_id: int, user:Annotated[UserDto, Depends(api_key_auth)]) -> IssueDto:
    return mock_data.generate_issue(str(issue_id))

@router.get("/", response_model=List[IssueDto])
async def get_all_issues(user:Annotated[UserDto, Depends(api_key_auth)]) -> List[IssueDto]:
    return mock_data.generate_issues_list()