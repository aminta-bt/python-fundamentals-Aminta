# python-fundamentals-Aminta
## Assignment 1

This repository contains collection of fundamental Python scripts developed as a foundation before transitioning to the Django & React.The project consists of five programming exercises that shows knowledge of data structures, input validation, string manipulation & file system processing.Every script ensures that unexpected user inputs generate clean, readable warnings rather than huge terminal crashes.

---

## Technical Setup & Verification

Before running the exercises, ensure your local environment is validated:
* **Python Version:** Compatible with Python 3.11 or newer.
* **Git Authentication:** Configured securely using SSH key-agent pairings to communicate with the GitHub.

---

## How to Run Each Exercise

All scripts can be run from the command line. Open your terminal inside Visual Studio Code & execute the commands below.

### Exercise 1: Temperature Converter
Converts user-specified temperature values between Celsius and Fahrenheit while validating numeric input.
```bash
python exercises/01_temperature.py
```

### Exercise 2: Word & Character Counter
Reads an external text asset (`sample.txt`) to dynamically calculate total characters, total words, and case-insensitive unique word counts, returning the final data inside a structured dictionary.
*Note: Ensure a text file named `sample.txt` exists in your main project folder before running*
```bash
python exercises/02_counter.py
```

### Exercise 3: Configurable FizzBuzz
An upgraded variation of the classic loop algorithm that takes function parameters directly from user. It includes validation gates to prevent crashes from non-numeric inputs or zero-division scenarios.
```bash
python exercises/03_fizzbuzz.py
```

### Exercise 4: In-Memory Contact Book
A menu-driven command-line program that manages contact entries using a list of dictionaries. It supports adding data, listing stored records, and applying case-insensitive lookup filters.
```bash
python exercises/04_contacts.py
```

### Exercise 5: Sales CSV Analysis
Utilizes Python's built-in `csv.DictReader` to parse metrics line-by-line from `sales.csv`. The program calculates total revenue, transactional averages, and identifies the highest-earning product using dictionary lookups.
*Note: Ensure a text file named `sales.csv` exists in your main project folder before running*
```bash
python exercises/05_sales.py
```

---

## What I Learned

* **Setting up an SSH Key:** Learned how to generate an SSH key and add it to the background agent to communicate securely with GitHub.
* **Writing Clear Commit Messages:** Avoided using messages like "update" or "final final" to write proper commit statements explaining what changed.
* **PEP 8 Style for Python:** Practiced following the official style guide for clean code formatting, spacing, and layout.
* **Optimizing Print Statements:** Learned how to use modern f-strings to format text and cleanly output variable values.
* **Pull Requests (PRs):** Introduced to the concept of how code branches are reviewed and merged into a main project.