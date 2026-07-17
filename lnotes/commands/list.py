from lnotes.storage.json_store import load_notes


def list_notes():

    notes = load_notes()

    if not notes:
        print("No notes found")

        return

    print("\nYour Notes:\n")

    for note in notes:
        print(f"{note['id']} - {note['title']}")
