# 📚 Day 076 — Introduction to SQLite

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 076  
**Topic:** Introduction to SQLite

---

# 1. What Is a Database?

A database is an organized collection of data that can be stored, accessed, updated, and managed efficiently.

Examples:

- Student records
- Course information
- Product details
- Customer information
- Orders
- Employee records

Instead of storing large amounts of structured information directly inside application code, applications commonly use databases.

---

# 2. What Is a DBMS?

DBMS stands for Database Management System.

A DBMS is software that allows applications and users to:

- Create databases
- Store data
- Retrieve data
- Update data
- Delete data
- Manage database structures

Examples include:

- SQLite
- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server

---

# 3. What Is a Relational Database?

A relational database stores data in tables.

A table contains:

- Rows
- Columns

For example, a student table might contain:

    students

    id | name   | course
    ---|--------|--------
    1  | Saloni | Python
    2  | Rahul  | Flask
    3  | Priya  | SQL

Each row represents one record.

Each column represents one attribute.

---

# 4. What Is SQLite?

SQLite is a lightweight relational database management system.

Unlike many database systems, SQLite does not require a separate database server for basic use.

The database is commonly stored as a single file.

Example:

    students.db

This makes SQLite convenient for:

- Learning
- Small applications
- Prototypes
- Local applications
- Testing
- Embedded systems

---

# 5. SQLite Is Serverless

Traditional database systems often use a separate database server.

SQLite works differently.

A simplified comparison:

    Traditional Database

    Application
        ↓
    Database Server
        ↓
    Database


    SQLite

    Application
        ↓
    SQLite Library
        ↓
    Database File

SQLite is therefore commonly described as serverless.

---

# 6. SQLite Database File

An SQLite database can be stored in a file.

Example:

    student.db

The file contains the database structures and data.

The application can open the database file and perform SQL operations.

---

# 7. SQLite and Python

Python includes the built-in `sqlite3` module.

Therefore, basic SQLite operations can be performed without installing a separate SQLite Python package.

Example:

    import sqlite3

    connection = sqlite3.connect("students.db")

---

# 8. Database Connection

The connection represents communication between the Python application and the SQLite database.

Example:

    import sqlite3

    connection = sqlite3.connect("students.db")

After the work is completed:

    connection.close()

---

# 9. Cursor

A cursor is used to execute SQL statements and retrieve results.

Example:

    cursor = connection.cursor()

Then:

    cursor.execute("SELECT * FROM students")

---

# 10. SQL

SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

Common SQL operations include:

- Create
- Insert
- Select
- Update
- Delete

These operations form the basis of CRUD.

---

# 11. CRUD

CRUD stands for:

| Letter | Operation |
|---|---|
| C | Create |
| R | Read |
| U | Update |
| D | Delete |

Database applications commonly perform these four operations.

---

# 12. CREATE TABLE

A table can be created using SQL.

Example:

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        course TEXT
    );

This creates a table named `students`.

---

# 13. Columns

The example contains three columns:

    id
    name
    course

Each column has a data type.

---

# 14. Common SQLite Data Types

SQLite commonly uses these storage classes:

| Type | Description |
|---|---|
| NULL | Missing or unknown value |
| INTEGER | Integer number |
| REAL | Floating-point number |
| TEXT | Text value |
| BLOB | Binary data |

SQLite's type system is flexible compared with some other relational databases.

---

# 15. Primary Key

A primary key uniquely identifies each row.

Example:

    id INTEGER PRIMARY KEY

For a student table:

    id | name
    ---|------
    1  | Saloni
    2  | Rahul

The `id` identifies each student record.

---

# 16. INSERT

The `INSERT` statement adds records.

Example:

    INSERT INTO students (name, course)
    VALUES ('Saloni', 'Python');

Multiple records can also be inserted.

---

# 17. SELECT

`SELECT` retrieves data.

Example:

    SELECT * FROM students;

To select specific columns:

    SELECT name, course
    FROM students;

---

# 18. WHERE

`WHERE` filters records.

Example:

    SELECT *
    FROM students
    WHERE course = 'Python';

Only matching records are returned.

---

# 19. UPDATE

`UPDATE` modifies existing records.

Example:

    UPDATE students
    SET course = 'Flask'
    WHERE id = 1;

The `WHERE` condition is very important.

Without an appropriate condition, multiple rows may be updated.

---

# 20. DELETE

`DELETE` removes records.

Example:

    DELETE FROM students
    WHERE id = 1;

Again, the `WHERE` condition should be used carefully.

---

# 21. Commit

After modifying a database, changes generally need to be committed.

Example:

    connection.commit()

This makes the transaction's changes persistent.

---

# 22. Python SQLite Example

A basic workflow is:

    import sqlite3

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            course TEXT
        )
    """)

    connection.commit()
    connection.close()

---

# 23. `IF NOT EXISTS`

This prevents an error when the table already exists.

Example:

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    );

---

# 24. Parameterized Queries

User input should not be directly concatenated into SQL.

Unsafe approach:

    query = "SELECT * FROM students WHERE name = '" + name + "'"

A safer approach uses placeholders:

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

Parameterized queries help protect against SQL injection.

---

# 25. Fetching Results

After a `SELECT`, results can be retrieved.

Fetch one row:

    cursor.fetchone()

Fetch multiple rows:

    cursor.fetchall()

Example:

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

---

# 26. SQLite with Flask

Flask can use SQLite as its database.

A simplified flow is:

    Browser
       ↓
    Flask Route
       ↓
    Python Logic
       ↓
    sqlite3
       ↓
    SQLite Database
       ↓
    Result
       ↓
    Flask Response

---

# 27. Flask Database Connection

A simple Flask route can connect to SQLite.

Example:

    import sqlite3

    @app.route("/students")
    def students():
        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students"
        )

        data = cursor.fetchall()

        connection.close()

        return str(data)

This is a basic learning example.

Larger Flask applications should organize database access more carefully.

---

# 28. SQLite Advantages

SQLite is useful because it is:

- Lightweight
- Simple
- Serverless
- File-based
- Easy to set up
- Portable
- Suitable for learning
- Good for small applications

---

# 29. SQLite Limitations

SQLite may not be the best choice for every application.

Limitations can include:

- Limited concurrency compared with larger database servers
- Less suitable for very large multi-user systems
- Server-level database management features are different from client-server DBMSs
- Scaling patterns differ from systems such as PostgreSQL

The correct database depends on the application requirements.

---

# 30. SQLite vs MySQL/PostgreSQL

| Feature | SQLite | MySQL/PostgreSQL |
|---|---|---|
| Server required | No | Yes |
| Storage | Database file | Server-managed database |
| Setup | Very easy | More setup |
| Small applications | Excellent | Excellent |
| Learning | Excellent | Excellent |
| Large multi-user systems | Limited | Better suited |

---

# 31. SQLite and Flask Development

SQLite is particularly convenient while learning Flask because:

- No database server is required.
- Python includes `sqlite3`.
- The database can be stored inside the project during development.
- SQL concepts can be practiced immediately.

Example project:

    flask_app/
    │
    ├── app.py
    ├── students.db
    ├── templates/
    └── static/

---

# 32. Important Database Rules

Always remember:

- Give tables meaningful names.
- Give columns meaningful names.
- Use primary keys where appropriate.
- Use parameterized queries.
- Commit changes.
- Close connections when appropriate.
- Validate user input.
- Do not trust user-provided SQL.
- Back up important databases.

---

# 33. Database Mental Model

Think of a database as:

    Database
       ↓
    Tables
       ↓
    Rows + Columns
       ↓
    SQL
       ↓
    Application

For Flask:

    Browser
       ↓
    Flask
       ↓
    Python
       ↓
    SQLite
       ↓
    Data
       ↓
    Flask
       ↓
    Browser

---

# ⭐ Key Takeaway

SQLite is a lightweight, serverless relational database system that stores data in a database file.

The basic Python workflow is:

    Connect
       ↓
    Create Cursor
       ↓
    Execute SQL
       ↓
    Fetch Results
       ↓
    Commit Changes
       ↓
    Close Connection

Understanding this workflow is the foundation for connecting Flask applications with databases.