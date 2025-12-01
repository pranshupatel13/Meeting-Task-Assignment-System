from typing import List, Dict
import re

class TaskAssigner:
    def __init__(self, team_members):
        """Initialize with team members for smart matching"""
        self.team_members = team_members
    
    def assign_tasks(self, tasks: List[Dict]) -> List[Dict]:
        """Assign unassigned tasks based on skills and keywords"""
        print("[INFO] Smart assignment starting...")
        
        for task in tasks:
            if not task.get('assigned_to'):
                assigned = self._find_best_match(task)
                task['assigned_to'] = assigned
                print(f"  Assigned Task {task['id']}: {assigned}")
        
        print(" All tasks assigned!")
        return tasks
    
    def _find_best_match(self, task: Dict) -> str:
        """Find best team member using skill matching"""
        description = task['description'].lower()
        best_member = None
        best_score = 0
        
        for member in self.team_members:
            score = self._calculate_match_score(description, member)
            
            if score > best_score:
                best_score = score
                best_member = member.name
        
        return best_member or "Unassigned"
    
    def _calculate_match_score(self, task_text: str, member) -> int:
        """Calculate skill/role match score (0-100)"""
        score = 0
        
        # Match skills (high weight)
        for skill in member.skills:
            if skill.lower() in task_text:
                score += 25  # Each skill match = 25 points
        
        # Match role keywords
        role_keywords = member.role.lower().split()
        for keyword in role_keywords:
            if keyword in task_text:
                score += 10
        
        # Bonus for action words matching role
        action_role_bonus = self._get_action_role_bonus(task_text, member.role.lower())
        score += action_role_bonus
        
        return min(score, 100)  # Cap at 100
    
    def _get_action_role_bonus(self, task_text: str, role: str) -> int:
        """Bonus points for role-specific actions"""
        bonuses = {
            'frontend': ['react', 'ui', 'javascript', 'frontend', 'bug'],
            'backend': ['database', 'api', 'performance', 'backend', 'server'],
            'designer': ['design', 'ui/ux', 'figma', 'mobile design'],
            'qa': ['test', 'testing', 'quality', 'qa']
        }
        
        for role_key, keywords in bonuses.items():
            if role_key in role:
                for keyword in keywords:
                    if keyword in task_text:
                        return 15
        return 0

# Test the assigner
if __name__ == "__main__":
    from utils import load_team_members
    
    # Load team
    team = load_team_members("data/team_members.json")
    assigner = TaskAssigner(team)
    
    # Sample tasks (some assigned, some not)
    # Sample tasks (FULL structure with all fields)
    sample_tasks = [
        {
            'id': 1,
            'description': 'Sakshi, fix the critical login bug - React component issue',
            'assigned_to': 'Sakshi',
            'priority': 'Critical',    
            'deadline': '2025-11-30'
        },
        {
            'id': 2,
            'description': 'Optimize database performance and API calls',
            'assigned_to': None,
            'priority': 'High',        
            'deadline': '2025-12-03'
        },
        {
            'id': 3,
            'description': 'Design new onboarding screens in Figma',
            'assigned_to': None,
            'priority': 'Medium',      
            'deadline': '2025-12-01'
        },
        {
            'id': 4,
            'description': 'Write unit tests for payment module',
            'assigned_to': None,
            'priority': 'Medium',       
            'deadline': '2025-12-03'
        }
    ]

    
    # Run assignment
    assigned_tasks = assigner.assign_tasks(sample_tasks)
    
    print("\n FINAL ASSIGNMENTS:")
    for task in assigned_tasks:
        print(f"Task {task['id']}: {task['description'][:50]}...")
        priority = task.get('priority', 'Medium')
        print(f"  👤 {task['assigned_to']} | {priority}")
        print()
