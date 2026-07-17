import sys

from lnotes.commands.add import add_note
from lnotes.commands.delete import delete_note
from lnotes.commands.list import list_notes
from lnotes.commands.search import search_notes
from lnotes.commands.update import update_note
from lnotes.commands.view import view_note


def main():

    if len(sys.argv) < 2:
        print(
            """
Usage:

lnotes add <title>

lnotes list
"""
        )

        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: lnotes add <title>")
            return

        title = sys.argv[2]

        add_note(title)

    elif command == "list":
        list_notes()

    elif command == "view":
        note_id = sys.argv[2]

        view_note(note_id)

    elif command == "delete":
        note_id = sys.argv[2]

        delete_note(note_id)

    elif command == "update":
        note_id = sys.argv[2]

        update_note(note_id)

    elif command == "search":
        keyword = sys.argv[2]

        search_notes(keyword)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
