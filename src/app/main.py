# Main file to run the application
from teams import create_teams, delete_all_teams
from rulesets import create_rulesets, delete_all_rulesets
import argparse


parser = argparse.ArgumentParser()

# Definir los argumentos
parser.add_argument("--delete", action="store_true", help="Delete all teams and rulesets")

args = parser.parse_args()



if __name__ == "__main__":

    if args.delete:
        delete_all_rulesets()
        delete_all_teams()
        print("All teams and rulesets deleted successfully")
    else:
        teams = create_teams()
        create_rulesets(teams[0].id, teams[1].id)
        print("Teams and rulesets created successfully")