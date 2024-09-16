from typing import Self

import requests

from dataclasses import dataclass
from requests import Response
from datetime import datetime
from dataclass_wizard import JSONWizard
from .users import user_one_token


class IssueClient:
    base_params = "v1/api/issues"
    base_url = f'http://localhost:8000/{base_params}'
    token: str = user_one_token

    def with_token(self, token:str) -> Self:
        self.token = token
        return self

    def get_issue(self, issue_id:int) -> Response:
        return self.__get_session().get(self.base_url + f'/{issue_id}')

    def get_issue_list(self) -> Response:
        return self.__get_session().get(self.base_url)

    def __get_session(self):
        s = requests.session()
        s.headers.update({"Authorization": f"Bearer {self.token}"})
        return s

@dataclass
class IssueDto(JSONWizard):
    id: str
    created_at: datetime
    author: str
    label: str
    description: str
    priority: int

