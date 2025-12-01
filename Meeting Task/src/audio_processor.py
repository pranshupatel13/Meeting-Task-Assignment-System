import speech_recognition as sr
import os
from pydub import AudioSegment

class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def get_transcript_text(self, audio_file_path):
        """Convert MP3/WAV/M4A to text using Google Speech Recognition"""
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
        
        print(f"[INFO] Processing audio: {os.path.basename(audio_file_path)}")
        
        # Convert to WAV (SpeechRecognition only supports WAV)
        audio = AudioSegment.from_file(audio_file_path)
        wav_path = "temp_audio.wav"
        audio.export(wav_path, format="wav")
        
        # Transcribe using Google STT (FREE)
        print("[INFO] Transcribing with Google Speech Recognition...")
        with sr.AudioFile(wav_path) as source:
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source)
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
        
        # Cleanup
        os.remove(wav_path)
        print(f"[INFO]  Transcription complete! ({len(text)} characters)")
        return text

# Test
if __name__ == "__main__":
    processor = AudioProcessor()
    print(processor.get_transcript_text("data/meeting.mp3"))
