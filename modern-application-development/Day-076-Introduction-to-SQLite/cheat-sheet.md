# ⚡ Day 076 — SQLite Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 076  
**Topic:** Introduction to SQLite

---

## 🔹 SQLite

SQLite is:

- Relational
- Lightweight
- Serverless
- File-based
- Easy to use

Example database:

    students.db

---

## 🔹 Python Module

    import sqlite3

Python provides `sqlite3` as a standard library module.

---

## 🔹 Connect

    connection = sqlite3.connect("students.db")

---

## 🔹 Cursor

    cursor = connection.cursor()

---

## 🔹 Create Table

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            course TEXT
        )
    """)

---

## 🔹 Insert

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        ("Saloni", "Python")
    )

---

## 🔹 Select

    cursor.execute(
        "SELECT * FROM students"
    )

---

## 🔹 Fetch One

    row = cursor.fetchone()

---

## 🔹 Fetch All

    rows = cursor.fetchall()

---

## 🔹 Update

    cursor.execute(
        "UPDATE students SET course = ? WHERE id = ?",
        ("Flask", 1)
    )

---

## 🔹 Delete

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (1,)
    )

---

## 🔹 Commit

    connection.commit()

Used to persist database changes.

---

## 🔹 Close

    connection.close()

---

## 🔹 CRUD

| Letter | Meaning | SQL |
|---|---|---|
| C | Create | INSERT |
| R | Read | SELECT |
| U | Update | UPDATE |
| D | Delete | DELETE |

---

## 🔹 SQLite Storage Classes

| Type | Meaning |
|---|---|
| NULL | Missing value |
| INTEGER | Integer |
| REAL | Floating-point |
| TEXT | Text |
| BLOB | Binary data |

---

## 🔹 Primary Key

    id INTEGER PRIMARY KEY

Uniquely identifies a row.

---

## 🔹 WHERE

    SELECT *
    FROM students
    WHERE id = 1;

Filters records.

---

## 🔐 Parameterized Query

Prefer:

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

Avoid constructing SQL by directly concatenating user input.

---

## 🔹 Flask + SQLite Flow

    Browser
       ↓
    Flask Route
       ↓
    Python
       ↓
    sqlite3
       ↓
    SQLite Database
       ↓
    Result
       ↓
    Response

---

## ⭐ Remember

`connect()` → Connect to database

`cursor()` → Create cursor

`execute()` → Execute SQL

`fetchone()` → Get one row

`fetchall()` → Get all rows

`commit()` → Save changes

`close()` → Close connection

`PRIMARY KEY` → Identify rows uniquely