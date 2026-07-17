import json
import sys
import uuid

NOTES_FILE = "notes.json"


# STORAGE FUNCTIONS


def load_notes():

    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_notes(notes):

    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


# ADD NOTE


def add_note(title):

    notes = load_notes()

    content = input("Enter content: ")

    note = {"id": str(uuid.uuid4()), "title": title, "content": content}

    notes.append(note)

    save_notes(notes)

    print("Note saved!")


# LIST NOTES


def list_notes():

    notes = load_notes()

    if not notes:
        print("No notes found")
        return

    print("\nYour Notes:\n")

    for note in notes:
        print(f"{note['id']}. {note['title']}")


# VIEW NOTE


def view_note(note_id):

    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            print(note["title"])
            print(note["content"])

            return

    print("Note not found")


# DELETE NOTE


def delete_note(note_id):

    notes = load_notes()

    updated = []

    for note in notes:
        if note["id"] != note_id:
            updated.append(note)

    save_notes(updated)

    print("Deleted")


# SEARCH TITLE


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
        print("No matching notes")


# UPDATE


def update_note(note_id):

    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            new_content = input("New content: ")

            note["content"] = new_content

            save_notes(notes)

            print("Updated")

            return

    print("Note not found")


# CLI HANDLER

if len(sys.argv) < 2:
    print(
        """
Usage:

lnotes add <title>

lnotes list

lnotes view <id>

lnotes delete <id>
"""
    )

    exit()


command = sys.argv[1]


# ADD

if command == "add":
    if len(sys.argv) < 3:
        print("Usage: lnotes add <title>")

        exit()

    title = sys.argv[2]

    add_note(title)

# UPDATE

elif command == "update":
    note_id = sys.argv[2]

    update_note(note_id)


# LIST

elif command == "list":
    list_notes()


# VIEW

elif command == "view":
    if len(sys.argv) < 3:
        print("Usage: lnotes view <id>")

        exit()

    note_id = int(sys.argv[2])

    view_note(note_id)

# SEARCH

elif command == "search":
    keyword = sys.argv[2]

    search_notes(keyword)

# DELETE

elif command == "delete":
    if len(sys.argv) < 3:
        print("Usage: lnotes delete <id>")

        exit()

    note_id = int(sys.argv[2])

    delete_note(note_id)


else:
    print("Unknown command")
