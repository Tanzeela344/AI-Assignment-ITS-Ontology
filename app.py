import tkinter as tk
from gui import main_gui
from database import initialize_db


def main():
    """Initialize the database and launch the GUI."""
    print("Initializing the Intelligent Tutoring System...")
    initialize_db()  # Set up the database
    print("Database initialized successfully.")

    # Launch the main GUI
    main_gui()
    print("Application closed.")


if __name__ == "__main__":
    main()
