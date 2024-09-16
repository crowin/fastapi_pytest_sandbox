from faker import Faker
from app.models.issue import IssueDto


faker = Faker()

def generate_issue(issue_id:str):

    return IssueDto(
        id = issue_id,
        created_at = faker.past_datetime(),
        author = faker.name(),
        label = f"'{faker.company()}' does not work for '{faker.address()}'",
        description = faker.text(100),
        priority = faker.random_int(1, 5)
    )

def generate_issues_list() -> list[IssueDto]:
    default_size = 20

    return [generate_issue(str(i)) for i in range(1, default_size + 1)]