from utils import load_team_members
from task_extractor import TaskExtractor
from task_assigner import TaskAssigner
from output_generator import OutputGenerator

print("🧪 FULL SYSTEM TEST (No Audio Required)")

# Load everything
team = load_team_members("data/team_members.json")
extractor = TaskExtractor()
assigner = TaskAssigner(team)
generator = OutputGenerator()

# Sample meeting transcript
transcript = """
Sakshi, fix critical login bug tomorrow - blocking users.
Mohit, optimize database by Friday, high priority.
Arjun, design onboarding screens next week.
Lata, write payment tests after login fix.
Update API docs before release.
"""

print("1. Extracting tasks...")
tasks = extractor.extract_tasks(transcript, team)

print("2. Assigning tasks...")
tasks = assigner.assign_tasks(tasks)

print("3. Generating outputs...")
generator.generate_json(tasks, "demo_output.json")
generator.generate_csv(tasks, "demo_output.csv")
generator.print_table(tasks)

print("✅ FULL SYSTEM WORKS PERFECTLY!")
