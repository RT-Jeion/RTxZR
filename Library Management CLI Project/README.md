# Library Management CLI Project

## Goal
Build a terminal-based app to manage a small library. Users can **add books, borrow/return books, view, search, and delete books**, with all data persisted in **JSON or CSV files**.

---

## 1. What This Project Can Do
- Store library book data (title, author, genre, ISBN, availability).  
- Add new books to the library.  
- Borrow or return books and track their status.  
- Search books by title, author, or ISBN.  
- Delete books from the library.  
- View all books or filter by availability or genre.  
- Persist library data in files between program runs.  
- Optional: track overdue books, sort books, show statistics.  

---

## 2. Features with Implementation Details

| Feature | What it does | Modules / Functions to Use |
|---------|-------------|---------------------------|
| **Add Book** | Add a new book with title, author, genre, ISBN, availability | `Book` class, `add_book()` method, `input()`, save to list and JSON/CSV |
| **View Books** | List all books; optionally filter by genre/author | Loop through book list, formatted `print()`, optional `tabulate` |
| **Borrow Book** | Mark book as borrowed, update availability, record borrower/date | Update `Book` object, `datetime` module for borrow date, save to file |
| **Return Book** | Mark book as returned, update availability | Update `Book` object, save to file |
| **Search Book** | Search by title, author, or ISBN | Loop + `if` statements, optional regex |
| **Delete Book** | Remove a book from library | Remove from list, save updated list |
| **Save & Load Library** | Persist library data between sessions | `json` or `csv` module, `open()`, `json.dump()` / `json.load()` |
| **Optional: Sort Books** | Sort by title, author, or genre | `sorted()` with `lambda` |
| **Optional: Statistics** | Show total books, borrowed, available | Count items in list with conditions |
| **Optional: Overdue Tracking** | Highlight books past due date | `datetime` module, compare borrow_date with current date |

---

## 3. Suggested OOP Structure

- **`Book` class**
  - Fields: `title`, `author`, `genre`, `ISBN`, `is_available`, `borrower_name` (optional), `borrow_date` (optional)  
  - Methods: `to_dict()`, `from_dict()`, optional `borrow()`, `return_book()`
  
- **`Library` class**
  - Field: `books` (list of `Book` objects)  
  - Methods:
    - `add_book()`, `delete_book()`, `borrow_book()`, `return_book()`  
    - `search_book()`, `view_books()`  
    - `save_library()`, `load_library()`
  
- **CLI / Main module**
  - Menu options: Add, View, Borrow, Return, Search, Delete, Exit  
  - Handles input, validation, and calls Library methods

---

## 4. Step-by-Step Plan for One Person

### Step 1: Setup
- Create folder with files:
  - `models.py` → Book & Library classes  
  - `cli.py` → menu system  
  - `library.json` → data storage  
- Import modules: `json`, `datetime`, `os`

### Step 2: Create `Book` Class
- Define fields: title, author, genre, ISBN, availability, borrower info  
- Methods: `to_dict()` for saving, `from_dict()` for loading, optional `borrow()` / `return_book()`

### Step 3: Create `Library` Class`
- Field: list of Book objects (`self.books`)  
- Methods:  
  - `add_book()` → append and save  
  - `delete_book()` → remove by title/ISBN  
  - `borrow_book()` → update availability, record borrower/date  
  - `return_book()` → update availability  
  - `search_book()` → search by title, author, ISBN  
  - `view_books()` → display books, optional filters  
  - `save_library()` / `load_library()` → JSON/CSV file handling

### Step 4: Build CLI Menu
- Options: Add, View, Borrow, Return, Search, Delete, Exit  
- Loop menu until exit  
- Validate user input  
- Call Library methods for each option

### Step 5: File Handling
- On startup: `load_library()`  
- After changes: `save_library()`  
- Use `json.dump()` / `json.load()` for saving/loading

### Step 6: Optional Enhancements
- Sort books alphabetically by title/author  
- Show statistics: total books, borrowed, available  
- Track overdue books: use `datetime` to compare borrow_date with current date  

---

## 5. Module / Function Map

| Task | Module / Function |
|------|-----------------|
| Save/load data | `json` module, `open()`, `json.dump()` / `json.load()` |
| Borrow/return date | `datetime` module, `datetime.date.today()` |
| Menu and input | `input()`, `print()`, `while` loop |
| Sorting books | `sorted()` with `lambda` |
| Optional colored output | `colorama` or ANSI codes |

---

## ✅ Summary Flow
1. Build `Book` class (data + methods)  
2. Build `Library` class (manage books + file handling)  
3. Implement CLI menu (`cli.py`)  
4. Test adding, borrowing, returning, deleting, searching  
5. Add optional features: sorting, stats, overdue tracking
