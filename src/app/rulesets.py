# Create a request to github api to set rules for the repository
import requests
import json
from constants import headers, organization_name


def create_rulesets(release_team_id: str, team_lead_id: str):

    rulesets = ["dev-test", "feature-task", "master"]

    for ruleset in rulesets:
        print(f"- Creating ruleset {ruleset}")

        with open(f"./src/json/{ruleset}.json") as file:
            rules = json.load(file)

            if ruleset == "dev-test":
                rules["bypass_actors"][0]["actor_id"] = team_lead_id

            if ruleset == "master":
                rules["bypass_actors"][0]["actor_id"] = release_team_id

        response = requests.post(
            f"https://api.github.com/orgs/{organization_name}/rulesets",
            headers=headers,
            data=json.dumps(rules)
        )


def delete_all_rulesets():

    response = requests.get(
        "https://api.github.com/orgs/FirstOrgt/rulesets", headers=headers
    )

    # Get all ids of the rulesets
    ruleset_ids = [ruleset["id"] for ruleset in response.json()]

    for id in ruleset_ids:
        print(f"- Deleting ruleset {id}")
        response = requests.delete(
            f"https://api.github.com/orgs/FirstOrgt/rulesets/{id}", headers=headers
        )
