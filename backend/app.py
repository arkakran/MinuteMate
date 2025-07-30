from flask import Flask, request, jsonify,render_template
from .listener import record_audio
from .whisper_transcriber import transcribe_audio
from .processor import summarize_transcript, extract_action_items
from .data_store import store

import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_meeting():
    try:
        audio_path = "audio/meeting.wav"
        record_audio(output_path=audio_path)
        transcript = transcribe_audio(audio_path)
        summary = summarize_transcript(transcript)
        actions, followups = extract_action_items(transcript)

        store.update(
            transcript=transcript,
            summary=summary,
            action_items=actions,
            follow_ups=followups
        )

        return jsonify({
            "status": "success",
            "message": "Meeting processed.",
            "summary": summary,
            "action_items": actions,
            "follow_ups": followups
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/results", methods=["GET"])
def get_results():
    return jsonify(store.get_all())

@app.route("/clear", methods=["POST"])
def clear_results():
    store.clear()
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    os.makedirs("audio", exist_ok=True)
    app.run(debug=True)
