import uuid

from lnotes.storage.json_store import load_notes, save_notes


def add_note(title):
    notes = load_notes()
    content = input("Enter content: ")
    note = {"id": str(uuid.uuid4()), "title": title, "content": content}

    notes.append(note)
    save_notes(notes)
    print("Note saved!")
