import pyaudio
import wave
import threading
import time
import numpy as np

class AudioRecorder:
    def __init__(self, output_path="audio/meeting.wav", silence_threshold=500, silence_duration=30):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.output_path = output_path
        self.silence_threshold = silence_threshold
        self.silence_duration = silence_duration
        self.recording = False
        self.frames = []

    def is_silent(self, data_chunk):
        audio_data = np.frombuffer(data_chunk, dtype=np.int16)
        return np.abs(audio_data).mean() < self.silence_threshold

    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.format,
                            channels=self.channels,
                            rate=self.rate,
                            input=True,
                            frames_per_buffer=self.chunk)

        print("🔴 Recording started... (Press Enter to stop manually)")
        self.recording = True
        self.frames = []
        silence_timer = 0

        while self.recording:
            data = stream.read(self.chunk)
            self.frames.append(data)

            if self.is_silent(data):
                silence_timer += self.chunk / self.rate
                if silence_timer >= self.silence_duration:
                    print("⏹️  Stopping due to silence...")
                    break
            else:
                silence_timer = 0

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(self.output_path, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))

        print(f"✅ Audio saved to: {self.output_path}")

    def start_background(self):
        thread = threading.Thread(target=self.record)
        thread.start()
        input()  
        self.recording = False
        thread.join()

def record_audio():
    recorder = AudioRecorder()
    recorder.start_background()

if __name__ == "__main__":
    record_audio()
