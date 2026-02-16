# Contact Book CLI Project – One-Person Plan

## Project Overview
A terminal-based contact manager where a user can **add, view, search, update, and delete contacts**, with data stored in **JSON or CSV files**.  
Practices **OOP, file handling, and modular coding**.

---

## 1. What This Project Can Do
- Store multiple contacts with:  
  - **Name**  
  - **Phone number**  
  - **Email**  
  - **Address** (optional)  
- View all contacts in a **neatly formatted list**  
- Search contacts by **name, phone, or email**  
- Update existing contact information  
- Delete contacts  
- Persist data between sessions with **JSON or CSV files**  
- Optional enhancements:  
  - Sort contacts alphabetically  
  - Export contacts as TXT reports  
  - Colored CLI for menus

---

## 2. Features, What They Do, and Required Modules

| Feature | Description | Python Modules / Concepts Needed |
|---------|-------------|---------------------------------|
| **Add Contact** | Add a new contact with all fields | OOP (`Contact` class), file handling (`json` or `csv`), input validation |
| **View All Contacts** | List all contacts in CLI table | Loops, string formatting, optional `tabulate` module, file read |
| **Search Contact** | Search by name, phone, or email | Loops, conditionals, string matching, file read |
| **Update Contact** | Modify fields of an existing contact | OOP (`ContactBook` class), input validation, file write |
| **Delete Contact** | Remove a contact by name/ID | Lists manipulation, file write, OOP |
| **Save & Load Data** | Automatically persist contacts in JSON or CSV | `json` or `csv` module, file read/write, exception handling |
| **Sort Contacts (Optional)** | Sort contacts alphabetically | `sorted()` function, lambda, file read/write |
| **Export TXT Report (Optional)** | Export contacts as a text file | File I/O (`open()`), string formatting |
| **Colored CLI (Optional)** | Color menus or search results | `colorama` module or ANSI codes |

---

## 3. Step-by-Step Workflow for One Person

### **Step 1: Setup**
- Create folder with files:  
  - `models.py` → `Contact` & `ContactBook` classes  
  - `cli.py` → main menu and user interaction  
  - `contacts.json` → data storage  
- Import necessary modules: `json`, `os`, optionally `colorama` or `tabulate`  

### **Step 2: Create `Contact` Class**
- Fields: `name`, `phone`, `email`, `address`  
- Methods: `to_dict()` for saving, `from_dict()` for loading  

### **Step 3: Create `ContactBook` Class**
- Field: list of `Contact` objects (`self.contacts`)  
- Implement methods:  
  - `add_contact()` → add contact to list  
  - `update_contact()` → modify existing contact  
  - `delete_contact()` → remove contact  
  - `search_contact()` → search by name/phone/email  
  - `view_contacts()` → display all contacts  
  - `save_to_file()` & `load_from_file()` → handle JSON/CSV storage  

### **Step 4: Build CLI Menu**
- Options: Add, View, Search, Update, Delete, Exit  
- Loop menu until exit  
- Validate input for all fields (phone, email, required fields)  
- Connect menu options to `ContactBook` methods  

### **Step 5: File Handling**
- On startup: call `load_from_file()`  
- After every change: call `save_to_file()`  
- Use `json.dump()` / `json.load()` for saving/loading  
- Add exception handling for missing or corrupt files  

### **Step 6: Optional Enhancements**
- Sort contacts alphabetically (`sorted()` with lambda)  
- Export contacts as TXT report (`open()` + string formatting)  
- Add colored menus or outputs (`colorama` or ANSI codes)  

---

## 4. Module / Function Map

| Task | Module / Function |
|------|-----------------|
| Save/load data | `json` or `csv`, `open()`, `json.dump()` / `json.load()` |
| Menu and input | `input()`, `print()`, `while` loop |
| Sorting contacts | `sorted()` with `lambda` |
| Display table | Optional: `tabulate` module |
| Colored CLI | Optional: `colorama` or ANSI codes |
| Input validation | Loops, conditionals, optional `re` module for regex |

---

## 5. Summary Flow
1. Build `Contact` class (data structure + methods)  
2. Build `ContactBook` class (manage list + file handling)  
3. Implement CLI menu (`cli.py`) with all options  
4. Test adding, searching, updating, deleting, saving/loading  
5. Add optional features: sorting, TXT export, colored CLI
