from lnotes.storage.json_store import load_notes, save_notes


def delete_note(note_id):

    notes = load_notes()

    updated_notes = []

    found = False

    for note in notes:
        if note["id"] == note_id:
            found = True

        else:
            updated_notes.append(note)

    if found:
        save_notes(updated_notes)

        print("Note deleted!")

    else:
        print("Note not found")
