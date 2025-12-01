from utils import load_team_members
import os

# Fix path to work from project root
team_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'team_members.json')

print(f"Looking for: {team_file}")
print(f"File exists: {os.path.exists(team_file)}")

# Test loading team data
if os.path.exists(team_file):
    team = load_team_members(team_file)
    print(" Team loaded successfully!")
    for member in team:
        print(f"- {member.name}: {member.role}")
else:
    print(" Create data/team_members.json first!")
