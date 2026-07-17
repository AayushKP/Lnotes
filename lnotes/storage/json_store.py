import json

NOTES_FILE = "notes.json"


def load_notes():

    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_notes(notes):

[]        json.dump(notes, file, indent=4)
