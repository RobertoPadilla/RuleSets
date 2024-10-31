import os
from dotenv import load_dotenv

load_dotenv()

organization_name = os.getenv("ORGANIZATION_NAME")
github_token = os.getenv("GITHUB_TOKEN")


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28",
}