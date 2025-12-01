import json
from typing import List, Dict

class TeamMember:
    def __init__(self, name, role, skills):
        self.name = name
        self.role = role
        self.skills = [s.lower() for s in skills]  # Normalize to lowercase
    
    def __repr__(self):
        return f"TeamMember({self.name}, {self.role})"

def load_team_members(json_file_path) -> List[TeamMember]:
    """Load team members from JSON file"""
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    team = []
    for member in data.get('team_members', []):
        tm = TeamMember(member['name'], member['role'], member['skills'])
        team.append(tm)
    
    return team

def save_json(data, file_path):
    """Save data to JSON file"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(file_path):
    """Load data from JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)
