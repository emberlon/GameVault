# GameVault
A Python application for organizing and tracking a personal video game collection.

## Planned features
 Add and remove games from a collection
 Search games by title
 Track platform, genre, release year, and completion status
 Sort games by title, platform, or release year
 Provide a graphical interface in a later sprint

## Data structures and algorithm
**Linked List:** stores the game collection.
**Hash Table:** indexes games by title for quick lookup.
**Insertion Sort:** custom sorting algorithm implemented in `algorithms/insertion_sort.py`.

The Linked List is the primary collection. The Hash Table stores references to the same `Game` objects.

## Project status
**Sprint 1: Foundation and planning**

The core model, data structures, sorting algorithm, and initial unit tests are being established. GUI work is planned for Sprint 2.

## Requirements
Python 3.10 or newer
No third-party packages required for the current starter version

## Run
From the project root:

python main.py

Run the tests:

python -m unittest discover -s tests -v

## Project structure
GameVault/
├── README.md
├── main.py
├── models/
│   ├── __init__.py
│   └── game.py
├── data_structures/
│   ├── __init__.py
│   ├── linked_list.py
│   └── hash_table.py
├── algorithms/
│   ├── __init__.py
│   └── insertion_sort.py
└── tests/
    ├── __init__.py
    ├── test_game.py
    ├── test_linked_list.py
    ├── test_hash_table.py
    └── test_insertion_sort.py
