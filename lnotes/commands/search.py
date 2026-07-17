from lnotes.storage.json_store import load_notes


def search_notes(keyword):

    notes = load_notes()

    found = False

    for note in notes:
        if keyword.lower() in note["title"].lower():
            print("\nFound:")

            print(note["title"])

            print(note["content"])

            found = True

    if not found:
        print("No notes found")
