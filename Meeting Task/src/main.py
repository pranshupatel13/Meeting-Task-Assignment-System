import argparse
import sys
from pathlib import Path
from audio_processor import AudioProcessor
from task_extractor import TaskExtractor
from task_assigner import TaskAssigner
from output_generator import OutputGenerator
from utils import load_team_members

def main():
    parser = argparse.ArgumentParser(description="🚀 Meeting Task Assignment System")
    parser.add_argument('--audio', required=True, help='Audio file (.wav, .mp3, .m4a)')
    parser.add_argument('--team', required=True, help='Team members JSON file')
    parser.add_argument('--output', default='output.json', help='Output JSON file')
    parser.add_argument('--format', choices=['json', 'csv', 'table', 'all'], default='all', help='Output format')
    
    args = parser.parse_args()
    
    print("MEETING TASK ASSIGNMENT SYSTEM")
    
    # Step 1: Validate inputs
    if not Path(args.audio).exists():
        print(f" Audio file not found: {args.audio}")
        sys.exit(1)
    
    if not Path(args.team).exists():
        print(f" Team file not found: {args.team}")
        sys.exit(1)
    
    print(f" Audio: {args.audio}")
    print(f" Team: {args.team}")
    print(f" Output: {args.output}")
    
    try:
        # Step 2: Load team
        print("\n [1/5] Loading team members...")
        team_members = load_team_members(args.team)
        print(f" Loaded {len(team_members)} team members")
        
        # Step 3: Transcribe audio OR load text file
        print("\n [2/5] Processing input...")
        processor = AudioProcessor()

        try:
            transcript = processor.get_transcript_text(args.audio)
        except Exception as e:
            # Fallback: treat as text file
            print(f" Audio failed ({e}), treating as text file...")
            try:
                with open(args.audio, 'r', encoding='utf-8', errors='ignore') as f:
                    transcript = f.read()
            except:
                transcript = "No transcript available"
        
        # Step 4: Extract tasks
        print("\n [3/5] Extracting tasks...")
        extractor = TaskExtractor()
        tasks = extractor.extract_tasks(transcript, team_members)
        print(f" Found {len(tasks)} tasks")
        
        # Step 5: Assign tasks
        print("\n [4/5] Smart assignment...")
        assigner = TaskAssigner(team_members)
        tasks = assigner.assign_tasks(tasks)
        
        # Step 6: Generate outputs
        print("\n [5/5] Generating outputs...")
        generator = OutputGenerator()
        
        if args.format in ['json', 'all']:
            generator.generate_json(tasks, args.output)
        if args.format in ['csv', 'all']:
            csv_file = args.output.replace('.json', '.csv')
            generator.generate_csv(tasks, csv_file)
        if args.format in ['table', 'all']:
            generator.print_table(tasks)
        
        print("SYSTEM COMPLETE! Check output files.")
        
    except Exception as e:
        print(f"\n ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
