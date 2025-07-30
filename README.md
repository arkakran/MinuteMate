# 📝 MinuteMate – Background Meeting Note Taker

MinuteMate is a background meeting assistant that:
- Listens to live meeting audio.
- Transcribes the meeting using Whisper.
- Summarizes the transcript.
- Extracts action items and follow-ups.
- Provides a simple web interface and REST API to interact with the results.

---

## 🔧 Features

- 🎤 Record real-time audio from your microphone.
- ✍️ Transcribe audio using OpenAI’s Whisper (via whisper-tiny model).
- 🧠 Extract key meeting summaries and action points using spaCy.
- 🗂️ Store and retrieve transcripts, summaries, and follow-ups.
- 🌐 Simple Flask web interface and API endpoints.

---

## 📁 Project Structure
MINUTEMATEE/
│
├── backend/
│ ├── app.py # Flask backend
│ ├── listener.py # Microphone audio recorder
│ ├── whisper_transcriber.py # Whisper-based transcription
│ ├── processor.py # NLP-based summarizer & action extractor
│ ├── data_store.py # In-memory data storage
│
├── templates/
│ └── index.html # Simple frontend UI
│
└── audio/
└── meeting.wav # Recorded audio file (auto-created)

create virtual environment and then activate it

pip install -r requirements.txt

pip install flask openai-whisper pyaudio spacy
python -m spacy download en_core_web_sm

python app.py



