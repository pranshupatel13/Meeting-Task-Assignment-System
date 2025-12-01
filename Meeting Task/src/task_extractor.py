import re
import nltk
from nltk.tokenize import sent_tokenize
from typing import List, Dict
from datetime import datetime, timedelta

# Download NLTK data if missing
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class TaskExtractor:
    def __init__(self):
        # Action keywords to identify tasks
        self.action_keywords = [
            'fix', 'build', 'create', 'design', 'optimize', 'update', 
            'implement', 'write', 'test', 'review', 'deploy', 'document',
            'refactor', 'debug', 'check', 'verify', 'improve', 'enhance'
        ]
        
        # Priority keywords
        self.priority_keywords = {
            'Critical': ['critical', 'blocker', 'blocking', 'urgent', 'asap'],
            'High': ['high', 'important', 'priority', 'soon', 'friday', 'release'],
            'Medium': ['medium', 'next', 'sprint', 'week'],
            'Low': ['low', 'later', 'backlog']
        }
        
        # Deadline patterns
        self.deadline_patterns = [
            ('tomorrow', 1),
            ('today', 0),
            ('tonight', 0),
            ('end of this week', 4),
            ('end of week', 4),
            ('friday', 'Friday'),
            ('wednesday', 'Wednesday'),
            ('monday', 'Monday'),
            ('next monday', 'Next Monday')
        ]
    
    def extract_tasks(self, transcript: str, team_members) -> List[Dict]:
        """Extract tasks from meeting transcript"""
        sentences = sent_tokenize(transcript)
        tasks = []
        task_id = 1
        
        print(f"[INFO] Analyzing {len(sentences)} sentences...")
        
        for sentence in sentences:
            if self._is_task_sentence(sentence):
                task = self._parse_task(sentence, team_members, task_id)
                if task:
                    tasks.append(task)
                    task_id += 1
        
        print(f" Extracted {len(tasks)} tasks!")
        return tasks
    
    def _is_task_sentence(self, sentence: str) -> bool:
        """Check if sentence contains task action keywords"""
        sentence_lower = sentence.lower()
        return any(keyword in sentence_lower for keyword in self.action_keywords)
    
    def _parse_task(self, sentence: str, team_members, task_id: int) -> Dict:
        """Parse task details from sentence"""
        task = {
            'id': task_id,
            'description': sentence.strip(),
            'assigned_to': None,
            'priority': 'Medium',
            'deadline': None,
            'dependencies': [],
            'reason': ''
        }
        
        # Extract priority
        for priority, keywords in self.priority_keywords.items():
            if any(keyword in sentence.lower() for keyword in keywords):
                task['priority'] = priority
                break
        
        # Extract deadline
        task['deadline'] = self._extract_deadline(sentence)
        
        # Extract assigned person
        task['assigned_to'] = self._extract_person(sentence, team_members)
        
        # Extract reason
        task['reason'] = self._extract_reason(sentence)
        
        return task
    
    def _extract_deadline(self, sentence: str) -> str:
        """Extract deadline from sentence"""
        sentence_lower = sentence.lower()
        for pattern, deadline in self.deadline_patterns:
            if pattern in sentence_lower:
                if isinstance(deadline, int):
                    future_date = datetime.now() + timedelta(days=deadline)
                    return future_date.strftime("%Y-%m-%d")
                return deadline
        return None
    
    def _extract_person(self, sentence: str, team_members) -> str:
        """Find mentioned team member"""
        sentence_lower = sentence.lower()
        for member in team_members:
            if member.name.lower() in sentence_lower:
                return member.name
        return None
    
    def _extract_reason(self, sentence: str) -> str:
        """Extract reason/context"""
        patterns = [r'(blocking|because|since|as)\s+([^\.]+)', r'affecting\s+([^\.]+)']
        for pattern in patterns:
            match = re.search(pattern, sentence.lower())
            if match:
                return match.group(2).strip()
        return sentence[:50] + "..."

# Test the extractor
if __name__ == "__main__":
    from utils import load_team_members
    
    extractor = TaskExtractor()
    team = load_team_members("data/team_members.json")
    
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
    
    tasks = extractor.extract_tasks(sample_transcript, team)
    
    for task in tasks:
        print(f"Task {task['id']}: {task['description']}")
        print(f"  Assigned: {task['assigned_to']} | Priority: {task['priority']} | Deadline: {task['deadline']}")
        print()
