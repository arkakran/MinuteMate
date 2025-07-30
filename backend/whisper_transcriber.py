import whisper

class WhisperTranscriber:
    def __init__(self, model_size="tiny"):
        print(f"📦 Loading Whisper model: {model_size} (this may take a few seconds)...")
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path="audio/meeting.wav"):
        print("🔍 Transcribing audio...")
        result = self.model.transcribe(audio_path)
        transcript = result['text'].strip()
        print("✅ Transcription complete.")
        return transcript

def transcribe_audio(audio_path="audio/meeting.wav"):
    transcriber = WhisperTranscriber()
    return transcriber.transcribe(audio_path)

if __name__ == "__main__":
    text = transcribe_audio()
    print("\n--- TRANSCRIPT ---\n")
    print(text)
