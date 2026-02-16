# Contact Book CLI Project – Full Plan

## Project Overview
A terminal-based contact manager where users can **add, view, search, update, and delete contacts**, with data stored in **JSON or CSV files**.  
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

## 3. Task Division Between Members

### **Member 1: RT Jeion – Backend / Logic**
**Responsibilities:**
- Build `Contact` class  
  - Fields: `name`, `phone`, `email`, `address`  
  - Methods: `to_dict()` and `from_dict()` for saving/loading  
- Build `ContactBook` class  
  - Manage list of contacts  
  - Features to implement:  
    - `add_contact()`  
    - `update_contact()`  
    - `delete_contact()`  
    - `search_contact()`  
    - `save_to_file()` & `load_from_file()`  
- Optional enhancements:  
  - Sort contacts (`sort_contacts()`)  
  - Handle exceptions for missing/corrupt files  

**Knowledge Needed:**  
- Python OOP, classes & methods  
- Lists, loops, conditionals  
- JSON/CSV file handling  

---

### **Member 2: Zubair – CLI / User Interface**
**Responsibilities:**
- Build main CLI menu  
  - Options: Add, View, Search, Update, Delete, Exit  
- Handle user input & validation  
  - Validate phone numbers, emails, and required fields  
- Display contacts neatly  
  - Pretty tables, headers, spacing  
  - Optional: `tabulate` or colored output  
- Integrate RT Jeion’s backend methods into menu options  
- Optional enhancements:  
  - Colored menus (`colorama`)  
  - Export TXT reports  

**Knowledge Needed:**  
- Loops, input(), string formatting  
- Conditional checks  
- Optional: Regex for validation, ANSI codes for colors  

---

## 4. Workflow & Collaboration
1. **Step 1 – RT Jeion:** Build classes (`Contact` & `ContactBook`) with basic methods + file handling.  
2. **Step 2 – Zubair:** Build CLI skeleton with menu options and dummy calls to methods.  
3. **Step 3 – Integration:** Connect CLI menu options to RT Jeion’s methods and test CRUD operations.  
4. **Step 4 – Optional Enhancements:**  
   - Sorting (RT Jeion)  
   - Colored CLI, TXT export (Zubair)  
5. **Step 5 – Testing & Debugging:** Both test adding, searching, updating, deleting, and saving/loading contacts.  

---

## 5. Summary of Responsibilities
| Member | Tasks |
|--------|-------|
| **RT Jeion** | Backend & logic: Classes, CRUD methods, file handling, optional sorting |
| **Zubair** | CLI & UX: Menu, input validation, display, integration, optional colored output/TXT export |
