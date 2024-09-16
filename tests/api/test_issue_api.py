from tests.api.client.issue_tracker_client import IssueClient, IssueDto
from test_base import unauthorized_error_code, bad_params_code, expected_ok_code

api = IssueClient()
expected_priority_range = range(1, 6)

def test_get_issue_positive():
    resp = api.get_issue(1)

    assert resp.status_code == expected_ok_code , 'Unexpected status code'

    actual_issue = IssueDto.from_dict(resp.json())

    assert actual_issue.priority in expected_priority_range, 'Unexpected priority range'

def test_get_issue_wrong_param():
    resp = api.get_issue('d')

    assert resp.status_code == bad_params_code , 'Unexpected status code'

def test_get_issue_wrong_token():
    resp = api.with_token("bad_token").get_issue(1)

    assert resp.status_code == unauthorized_error_code , 'Unexpected status code'

def test_get_issues_list():
    resp = api.get_issue_list()

    assert resp.status_code == expected_ok_code , 'Unexpected status code'

    actual_issues = IssueDto.from_list(resp.json())

    assert len(actual_issues) == 20
    assert actual_issues[0].priority in expected_priority_range

def test_get_issues_list():
    resp = api.with_token("bad_token").get_issue_list()

    assert resp.status_code == unauthorized_error_code , 'Unexpected status code'