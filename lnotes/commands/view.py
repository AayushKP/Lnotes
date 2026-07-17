from lnotes.storage.json_store import load_notes


def view_note(note_id):

    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            print("\nTitle:")
            print(note["title"])

            print("\nContent:")
            print(note["content"])

            return

    print("Note not found")
