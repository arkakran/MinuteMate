# backend/data_store.py

class DataStore:
    def __init__(self):
        self.data = {
            "transcript": "",
            "summary": "",
            "action_items": [],
            "follow_ups": []
        }

    def update(self, transcript=None, summary=None, action_items=None, follow_ups=None):
        if transcript is not None:
            self.data["transcript"] = transcript
        if summary is not None:
            self.data["summary"] = summary
        if action_items is not None:
            self.data["action_items"] = action_items
        if follow_ups is not None:
            self.data["follow_ups"] = follow_ups

    def get_all(self):
        return self.data

    def clear(self):
        self.data = {
            "transcript": "",
            "summary": "",
            "action_items": [],
            "follow_ups": []
        }

# Create a singleton instance
store = DataStore()
