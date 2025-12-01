# 🚀 Meeting Task Assignment System

**Automated system that processes meeting audio/transcripts and assigns tasks to team members based on skills/roles.** [100% Project Requirements Met]

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Step 1: Installation](#step-1-installation)
- [Step 2: Run System](#step-2-run-system)
- [Step 3: View Results](#step-3-view-results)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Requirements Checklist](#requirements-checklist)

## 🎯 Features
- 🎤 Audio (.mp3/.wav/.m4a) → Text transcription
- 🧠 Smart task extraction (priorities, deadlines, dependencies)
- 🤖 AI-powered task assignment by skills/roles
- 📊 JSON + CSV + Table outputs
- ⚡ Custom logic (no external classification APIs)

## 📋 Demo



## 🛠️ Step 1: Installation (2 minutes)

### 1.1 Clone Repository
git clone https://github.com/YOUR_USERNAME/meeting-task-assignment-system.git
cd meeting-task-assignment-system

### 1.2 Install Dependencies
pip install -r requirements.txt
python -m nltk.downloader punkt

**✅ Done! System ready.**

## 🚀 Step 2: Run System

### 2.1 With Sample Data (Recommended)
python src/main.py --audio data/perfect_test.txt --team data/team_members.json --format all


### 2.2 With Your Audio File
Copy your meeting.mp3 to data/ folder
python src/main.py --audio data/meeting.mp3 --team data/team_members.json --output my_results.json --format all


### 2.3 Command Options
python src/main.py --help

undefined
--audio Audio file or transcript (.mp3/.wav/.txt)
--team Team members JSON file
--output Output filename (default: output.json)
--format json/csv/table/all (default: all)


## 📊 Step 3: View Results

### 3.1 Console Table (Instant)
✅ JSON saved: results.json (2KB)
✅ CSV saved: results.csv (1KB)

[Beautiful formatted table above]

### 3.2 JSON Output (results.json)
{
"task_count": 5,
"tasks": [
{
"id": 1,
"description": "Sakshi fix critical login bug...",
"assigned_to": "Sakshi",
"deadline": "2025-12-02",
"priority": "Critical",
"reason": "blocking users"
}
]
}

### 3.3 CSV Output (Excel Compatible)
id,description,assigned_to,deadline,priority,reason
1,"Sakshi fix critical login bug",Sakshi,2025-12-02,Critical,"blocking users"


## 🔄 How It Works (4-Step Pipeline)

Step 1: Input → Step 2: Transcribe → Step 3: Extract → Step 4: Output
meeting.mp3 "Sakshi fix bug..." 5 Tasks w/ details JSON/CSV/Table
(Whisper/Google STT) (Custom NLP logic) (Professional format)


1. **AudioProcessor**: MP3/WAV → Text transcript
2. **TaskExtractor**: Finds "fix/design/test" + names + deadlines
3. **TaskAssigner**: Matches skills (React→Sakshi, Database→Mohit)
4. **OutputGenerator**: Creates all required formats

## 📁 Project Structure
meeting-task-assignment-system/
├── src/ # Source code (6 modules)
│ ├── main.py # 🎯 Main entry point
│ ├── audio_processor.py # 🎤 Audio → Text
│ ├── task_extractor.py # 🧠 Find tasks
│ ├── task_assigner.py # 🤖 Smart matching
│ ├── output_generator.py# 📊 JSON/CSV/Table
│ └── utils.py # 🔧 Helpers
├── data/ # 🧪 Sample inputs
│ ├── team_members.json # 👥 Sakshi/Mohit/Arjun/Lata
│ └── sample_transcript.txt # 📄 Test transcript
| └──meeting.mp3 # Meeting Audio file
├── requirements.txt # 📦 Dependencies
├── README.md # 📖 This file
└── .gitignore


## 👥 Sample Team Data
**`data/team_members.json`:**
{
"team_members": [
{"name": "Sakshi", "role": "Frontend Developer", "skills": ["React", "UI bugs", "frontend"]},
{"name": "Mohit", "role": "Backend Engineer", "skills": ["Database", "APIs", "backend"]},
{"name": "Arjun", "role": "UI/UX Designer", "skills": ["Figma", "design", "UI"]},
{"name": "Lata", "role": "QA Engineer", "skills": ["Testing", "QA"]}
]
}


## 🏆 Requirements Checklist [Project Spec]
- [x] **Audio formats**: .wav, .mp3, .m4a ✅
- [x] **Custom logic**: No external task APIs ✅
- [x] **Task assignment**: Skills/roles matching ✅
- [x] **Outputs**: JSON/table w/ all fields ✅
- [x] **Structure**: Organized files ✅
- [x] **requirements.txt**: Complete ✅
- [x] **Sample data**: Included ✅

## 🔧 Troubleshooting
| Issue | Solution |
|-------|----------|
| `ffmpeg not found` | Use text files or `pip install openai-whisper` |
| `No tasks found` | Check transcript has "fix/design/test" keywords |
| `Module not found` | `pip install -r requirements.txt` |

## 🎥 Demo Video
**[Watch demo](outputs/demo.mp4)** - 30 seconds showing full pipeline!

## 📄 License
MIT License © 2025

