# Create a request to github api to set rules for the repository
from typing import List
import requests
import json

from constants import headers, organization_name




class Team:
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id


def create_teams() -> List[Team]:
    # Teams to create
    teams = [
        Team("mig45939 Team Leads", "Aprueba PRs en las ramas dev y test", ""),
        Team("mig45939 Release Team", "Aprueba PRs en la rama master", "")
    ]

    # Using the github api to create the teams
    for team in teams:
        print(f"- Creating team {team.name}")
        request_json = {
            "name": team.name,
            "description": team.description,
            "permission": "push",
            "notification_setting": "notifications_enabled",
            "privacy": "closed"
        }

        response = requests.post(
            f"https://api.github.com/orgs/{organization_name}/teams",
            headers=headers,
            data=json.dumps(request_json),
        )

        team.id = response.json()["id"]
        
    return teams


def delete_all_teams():
    # Get all teams
    response = requests.get(f"https://api.github.com/orgs/{organization_name}/teams", headers=headers)

    # Get all slugs of the teams
    team_slugs = [team['slug'] for team in response.json()]

    for slug in team_slugs:
        print(f"- Deleting team {slug}")
        response = requests.delete(f"https://api.github.com/orgs/{organization_name}/teams/{slug}", headers=headers)
