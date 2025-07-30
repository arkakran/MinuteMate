# backend/processor.py

import spacy
from typing import List, Tuple

# Load English spaCy model
nlp = spacy.load("en_core_web_sm")


def summarize_transcript(text: str, max_sentences: int = 3) -> str:
    """Return a simple extractive summary using sentence scoring based on token count."""
    doc = nlp(text)
    sentences = list(doc.sents)

    # Score sentences by length and named entities
    ranked = sorted(
        sentences,
        key=lambda s: len(s.ents) + len(s.text.split()),
        reverse=True
    )

    summary = " ".join([sent.text for sent in ranked[:max_sentences]])
    return summary


def extract_action_items(text: str) -> Tuple[List[str], List[str]]:
    """Extract action items and follow-ups from transcript based on simple rules."""
    doc = nlp(text)
    action_items = []
    follow_ups = []

    for sent in doc.sents:
        lower = sent.text.lower()
        if any(trigger in lower for trigger in ["will", "need to", "should", "must", "to do", "plan to"]):
            action_items.append(sent.text.strip())
        elif any(trigger in lower for trigger in ["follow up", "remind", "check back", "ping", "circle back"]):
            follow_ups.append(sent.text.strip())

    return action_items, follow_ups
