# Music Quiz Application (GCSE Project)

A Python-based interactive command-line application designed to test general music knowledge. This project was originally developed as part of my GCSE coursework to demonstrate proficiency in programming fundamentals, including file handling, user authentication, and data persistence.

## Project Overview

The application is a quiz game where users can log in, answer questions about various songs, and have their scores recorded on a leaderboard. It was designed to meet specific client requirements for a school-based competition system.

**Key Objectives:**
* To build a robust user authentication system.
* To manage external data sources (songs and user scores) using JSON.
* To implement error handling and input validation for a smooth user experience.

## Key Features

* **User Authentication:** A secure login system that verifies usernames and passwords against a stored database (`logins.json`).
* **Dynamic Content:** Quiz questions are loaded from an external file (`songs.json`), allowing for easy updates without modifying the source code.
* **Persistent Leaderboard:** High scores are tracked and saved to `scorers.json`, preserving data between sessions.
* **Admin Utilities:** Includes scripts like `import to list.py` to help manage and format the song database.

## Technical Implementation

* **Language:** Python 3.x
* **Data Storage:** JSON (JavaScript Object Notation) for lightweight, structured data storage.
* **Architecture:** Modular design separating the main game logic (`Song Quiz.py`) from data management scripts.

### File Structure
* `Song Quiz.py` - The main executable containing the game loop and logic.
* `songs.json` - Database of songs, artists, and genre information.
* `logins.json` - User credentials database.
* `scorers.json` - Storage for user high scores.
* `import to list.py` - Utility script for importing new song data into the JSON structure.

## Getting Started

To run this application locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Big-Barry/music-GCSE-2021.git](https://github.com/Big-Barry/music-GCSE-2021.git)
    cd music-GCSE-2021
    ```

2.  **Run the application:**
    ```bash
    python "Song Quiz.py"
    ```

3.  **Usage:**
    Follow the on-screen prompts to log in (or create a user if applicable) and start the quiz.

## Key Takeaways

This project was a significant milestone in my early programming development. It taught me the importance of:
* **Separation of Concerns:** Keeping data (JSON) separate from logic (Python).
* **Data Integrity:** Ensuring that user inputs do not crash the program or corrupt data files.
* **Maintainability:** Writing code that can be easily extended (e.g., adding new songs via the external file rather than hardcoding them).

---
*This repository serves as an archive of my GCSE coursework.*
