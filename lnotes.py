import json
import sys

NOTES_FILE = "notes.json"


# -------------------------
# STORAGE FUNCTIONS
# -------------------------


def load_notes():

    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_notes(notes):

    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


# -------------------------
# ADD NOTE
# -------------------------


def add_note(title):

    notes = load_notes()

    content = input("Enter content: ")

    note = {"id": len(notes) + 1, "title": title, "content": content}

    notes.append(note)

    save_notes(notes)

    print("Note saved!")


# -------------------------
# LIST NOTES
# -------------------------


def list_notes():

    notes = load_notes()

    if not notes:
        print("No notes found")
        return

    print("\nYour Notes:\n")

    for note in notes:
        print(f"{note['id']}. {note['title']}")


# -------------------------
# VIEW NOTE
# -------------------------


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


# -------------------------
# DELETE NOTE
# -------------------------


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


# -------------------------
# CLI HANDLER
# -------------------------

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


# DELETE

elif command == "delete":
    if len(sys.argv) < 3:
        print("Usage: lnotes delete <id>")

        exit()

    note_id = int(sys.argv[2])

    delete_note(note_id)


else:
    print("Unknown command")
