import argparse

from lnotes.commands.add import add_note
from lnotes.commands.delete import delete_note
from lnotes.commands.list import list_notes
from lnotes.commands.search import search_notes
from lnotes.commands.update import update_note
from lnotes.commands.view import view_note


def main():

    parser = argparse.ArgumentParser(prog="lnotes", description="Linux Notes CLI")

    subparsers = parser.add_subparsers(dest="command")

    # ADD

    add_parser = subparsers.add_parser("add", help="Add a new note")

    add_parser.add_argument("title", help="Note title")

    # LIST

    subparsers.add_parser("list", help="List all notes")

    # VIEW

    view_parser = subparsers.add_parser("view", help="View a note")

    view_parser.add_argument("id", help="Note ID")

    # DELETE

    delete_parser = subparsers.add_parser("delete", help="Delete a note")

    delete_parser.add_argument("id", help="Note ID")

    # UPDATE

    update_parser = subparsers.add_parser("update", help="Update note")

    update_parser.add_argument("id", help="Note ID")

    # SEARCH

    search_parser = subparsers.add_parser("search", help="Search notes")

    search_parser.add_argument("keyword", help="Search keyword")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.title)

    elif args.command == "list":
        list_notes()

    elif args.command == "view":
        view_note(args.id)

    elif args.command == "delete":
        delete_note(args.id)

    elif args.command == "update":
        update_note(args.id)

    elif args.command == "search":
        search_notes(args.keyword)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
