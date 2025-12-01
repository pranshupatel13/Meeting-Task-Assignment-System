import json
import pandas as pd
from typing import List, Dict
from datetime import datetime

class OutputGenerator:
    @staticmethod
    def generate_json(tasks: List[Dict], output_file: str = "../output.json"):
        """Generate JSON output matching project requirements"""
        output_data = {
            'generated_at': datetime.now().isoformat(),
            'task_count': len(tasks),
            'tasks': tasks
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f" JSON saved: {output_file}")
        return output_file
    
    @staticmethod
    def generate_csv(tasks: List[Dict], output_file: str = "../output.csv"):
        """Generate CSV output with proper columns"""
        df = pd.DataFrame(tasks)
        
        # Standardize columns (match project spec)
        columns = ['id', 'description', 'assigned_to', 'deadline', 'priority', 'dependencies', 'reason']
        df = df.reindex(columns=[col for col in columns if col in df.columns], fill_value='')
        
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f" CSV saved: {output_file}")
        return output_file
    
    @staticmethod
    def print_table(tasks: List[Dict]):
        """Print beautiful console table"""
        df = pd.DataFrame(tasks)
        columns = ['id', 'description', 'assigned_to', 'deadline', 'priority', 'dependencies', 'reason']
        df = df.reindex(columns=[col for col in columns if col in df.columns], fill_value='')
        
        print("\n" + "="*100)
        print(" MEETING TASK ASSIGNMENTS")
        print("="*100)
        print(df.to_string(index=False))
        print("="*100)
    
    @staticmethod
    def generate_summary(tasks: List[Dict]) -> Dict:
        """Generate task summary statistics"""
        priorities = {}
        assignees = {}
        
        for task in tasks:
            prio = task.get('priority', 'Medium')
            priorities[prio] = priorities.get(prio, 0) + 1
            
            assignee = task.get('assigned_to', 'Unassigned')
            assignees[assignee] = assignees.get(assignee, 0) + 1
        
        return {
            'total_tasks': len(tasks),
            'priorities': priorities,
            'assignees': assignees
        }

# Test the output generator
if __name__ == "__main__":
    from utils import load_team_members
    from task_extractor import TaskExtractor
    from task_assigner import TaskAssigner
    
    print(" Testing Output Generator...")
    
    # Load data and process
    team = load_team_members("data/team_members.json")
    extractor = TaskExtractor()
    assigner = TaskAssigner(team)
    
    sample_transcript = """
    Hi everyone, let's discuss this week's priorities.

    Sakshi, we need someone to fix the critical login bug that users reported yesterday. 
    This needs to be done by tomorrow evening since it's blocking users.

    Also, the database performance is really slow, Mohit you're good with backend 
    optimization right? We should tackle this by end of this week, it's affecting the user experience.

    And we need to update the API documentation before Friday's release - this is high 
    priority.

    Oh, and someone should design the new onboarding screens for the next sprint. 
    Arjun, didn't you work on UI designs last month? This can wait until next Monday.

    One more thing - we need to write unit tests for the payment module. 
    This depends on the login bug fix being completed first, so let's plan this for Wednesday.
    """
    
    # Extract → Assign → Output
    tasks = extractor.extract_tasks(sample_transcript, team)
    tasks = assigner.assign_tasks(tasks)
    
    generator = OutputGenerator()
    
    # Generate all outputs
    generator.generate_json(tasks)
    generator.generate_csv(tasks)
    generator.print_table(tasks)
    
    # Show summary
    summary = generator.generate_summary(tasks)
    print("\n SUMMARY:")
    print(f"Total Tasks: {summary['total_tasks']}")
    print(f"Priorities: {summary['priorities']}")
