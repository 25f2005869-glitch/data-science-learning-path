# ⚡ Day 077 — Database Design and Tables Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 077  
**Topic:** Database Design and Tables

---

## 🔹 Basic Terms

`Database` → Collection of organized data

`Table` → Stores related records

`Row` → One record

`Column` → One attribute

`Entity` → Object about which data is stored

`Attribute` → Property of an entity

---

## 🔹 SQLite Data Types

| Type | Meaning |
|---|---|
| NULL | Missing/unknown value |
| INTEGER | Whole number |
| REAL | Floating-point number |
| TEXT | Text |
| BLOB | Binary data |

---

## 🔹 Primary Key

    id INTEGER PRIMARY KEY

Purpose:

- Uniquely identifies rows.
- Prevents duplicate primary-key values.
- Provides a stable reference for related records.

---

## 🔹 Foreign Key

    FOREIGN KEY (student_id)
    REFERENCES students(id)

Connects one table to another.

SQLite foreign-key enforcement should be enabled on the connection:

    PRAGMA foreign_keys = ON

---

## 🔹 NOT NULL

    name TEXT NOT NULL

The column cannot contain NULL.

---

## 🔹 UNIQUE

    email TEXT UNIQUE

Prevents duplicate values for the constrained column.

---

## 🔹 DEFAULT

    status TEXT DEFAULT 'active'

Provides a default value.

---

## 🔹 CHECK

    marks INTEGER
        CHECK (marks >= 0 AND marks <= 100)

Enforces a condition.

---

## 🔹 Create Table

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    );

---

## 🔹 IF NOT EXISTS

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    );

---

## 🔹 One-to-One

    Student ↔ Profile

One record relates to one record.

---

## 🔹 One-to-Many

    Course
      ↓
    Students

One record can relate to many records.

---

## 🔹 Many-to-Many

    Students ↔ Courses

Usually requires a junction table.

---

## 🔹 Junction Table

    enrollments

    student_id
    course_id

Example:

    CREATE TABLE enrollments (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id)
            REFERENCES students(id),
        FOREIGN KEY (course_id)
            REFERENCES courses(id)
    );

---

## 🔹 Composite Primary Key

    PRIMARY KEY (student_id, course_id)

Uses multiple columns together as the primary key.

---

## 🔹 Database Design Flow

    Requirements
        ↓
    Entities
        ↓
    Attributes
        ↓
    Primary Keys
        ↓
    Relationships
        ↓
    Foreign Keys
        ↓
    Constraints
        ↓
    Tables

---

## 🔐 Good Design Rules

- Use meaningful names.
- Use primary keys.
- Use foreign keys for relationships.
- Choose suitable data types.
- Use constraints.
- Avoid unnecessary duplication.
- Use junction tables for many-to-many relationships.
- Avoid repeated columns such as `course1`, `course2`, `course3`.

---

## ⭐ Remember

Primary Key → Identifies a row

Foreign Key → Connects tables

NOT NULL → Value required

UNIQUE → No duplicate values

DEFAULT → Automatic default value

CHECK → Enforces a condition

Junction Table → Represents many-to-many relationships