from lnotes.storage.json_store import load_notes, save_notes


def update_note(note_id):

    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            content = input("New content: ")

            note["content"] = content

            save_notes(notes)

            print("Note updated!")

            return

    print("Note not found")
