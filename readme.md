<img width="1014" height="743" alt="image" src="https://github.com/user-attachments/assets/bc997dce-8713-4202-89af-c213f8c1ed4c" />

# Linux Notes CLI

A simple command-line note-taking application built with Python. This project demonstrates how to build a professional CLI application with a modular architecture, JSON storage, and command-based interactions.

## Features

- Add notes
- List all notes
- View a note
- Update a note
- Delete a note
- Search notes by title
- UUID-based note IDs
- Modular project structure
- Installable as a CLI command

---

## Project Structure

```text
linux-cli/
│
├── setup.py
├── notes.json
│
└── lnotes/
    ├── __init__.py
    ├── main.py
    │
    ├── commands/
    │   ├── __init__.py
    │   ├── add.py
    │   ├── list.py
    │   ├── view.py
    │   ├── update.py
    │   ├── delete.py
    │   └── search.py
    │
    └── storage/
        ├── __init__.py
        └── json_store.py
```

---

# Prerequisites

- Python 3.10 or later
- pip

Verify installation:

```bash
python --version
pip --version
```

---

# Clone the Repository

```bash
git clone <repository-url>
```

Go into the project directory:

```bash
cd linux-cli
```

---

# Create a Virtual Environment (Recommended)

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install the Project

Install in editable mode:

```bash
pip install -e .
```

This creates the `lnotes` command on your system.

Verify installation:

```bash
lnotes --help
```

---

# First-Time Setup

Create a file named:

```text
notes.json
```

with the following content:

```json
[]
```

---

# Usage

## Show Help

```bash
lnotes --help
```

---

## Add a Note

```bash
lnotes add Linux
```

Example prompt:

```text
Enter content:
Linux is an open source operating system
```

---

## List Notes

```bash
lnotes list
```

Example:

```text
Your Notes:

7eeb9c8d-... - Linux
9abfcb9a-... - Docker
```

---

## View a Note

```bash
lnotes view <NOTE_ID>
```

Example:

```bash
lnotes view 7eeb9c8d-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

## Update a Note

```bash
lnotes update <NOTE_ID>
```

Example:

```text
New content:
Linux kernel manages hardware resources.
```

---

## Delete a Note

```bash
lnotes delete <NOTE_ID>
```

---

## Search Notes

```bash
lnotes search Linux
```

---

# Development

Run without installing:

```bash
python -m lnotes.main --help
```

Example:

```bash
python -m lnotes.main add Docker
```

---

# Common Issues

## `ModuleNotFoundError: No module named 'lnotes'`

Reinstall the package:

```bash
pip uninstall linux-notes-cli
pip install -e .
```

Ensure the following files exist:

```text
lnotes/__init__.py
lnotes/commands/__init__.py
lnotes/storage/__init__.py
```

---

# Technologies Used

- Python
- argparse
- json
- uuid
- setuptools

---
