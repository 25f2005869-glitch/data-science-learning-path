# 📚 Day 077 — Database Design and Tables

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 077  
**Topic:** Database Design and Tables

---

# 1. What Is Database Design?

Database design is the process of deciding:

- What data needs to be stored.
- How data should be organized.
- Which tables are required.
- Which columns each table should contain.
- How tables are related.
- Which constraints should be applied.

Good database design makes applications easier to maintain and reduces unnecessary duplication.

---

# 2. What Is a Table?

A relational database stores data in tables.

Example:

    students

    id | name   | email
    ---|--------|--------------------
    1  | Saloni | saloni@example.com
    2  | Rahul  | rahul@example.com

A table contains rows and columns.

---

# 3. Rows

A row represents one record.

Example:

    1 | Saloni | saloni@example.com

This represents one student.

A row is also called a record or tuple.

---

# 4. Columns

A column represents an attribute of the data.

For a student table:

    id
    name
    email
    course

Each column describes one property of a student.

---

# 5. Entity

An entity is something about which we want to store information.

Examples:

- Student
- Course
- Product
- Customer
- Order
- Employee

For a student management application:

    Student

can be an entity.

---

# 6. Attributes

Attributes describe an entity.

For Student:

    Student
       ↓
    id
    name
    email
    phone
    course

These are attributes of the Student entity.

---

# 7. Choosing Tables

A database should normally separate different types of information into appropriate tables.

For example:

    students
    courses
    enrollments

Instead of putting every piece of information into one large table.

---

# 8. Example Student Database

A simple design can contain:

    students
    courses
    enrollments

Students:

    id
    name
    email

Courses:

    id
    name
    credits

Enrollments:

    id
    student_id
    course_id

---

# 9. Primary Key

A primary key uniquely identifies each row.

Example:

    id INTEGER PRIMARY KEY

Student table:

    id | name
    ---|------
    1  | Saloni
    2  | Rahul

The IDs distinguish the records.

---

# 10. Properties of a Primary Key

A primary key should:

- Identify a row uniquely.
- Not contain duplicate values.
- Normally not be NULL.
- Be stable and meaningful for database design.

A table should have one primary key definition, which can consist of one or more columns.

---

# 11. Foreign Key

A foreign key references a key in another table.

Example:

    students

    id | name
    ---|------
    1  | Saloni


    enrollments

    id | student_id | course_id
    ---|------------|----------
    1  | 1          | 10

Here:

    enrollments.student_id

can reference:

    students.id

---

# 12. Why Foreign Keys Are Useful

Foreign keys help represent relationships between tables.

They can also help maintain referential integrity by preventing references to records that do not exist, when foreign key enforcement is enabled.

---

# 13. SQLite Foreign Key Enforcement

SQLite supports foreign keys, but applications should explicitly enable foreign key enforcement for each database connection.

Example:

    connection.execute("PRAGMA foreign_keys = ON")

This is important when relying on foreign key constraints.

---

# 14. Data Types

SQLite uses storage classes including:

| Type | Purpose |
|---|---|
| NULL | Missing value |
| INTEGER | Whole numbers |
| REAL | Floating-point numbers |
| TEXT | Text |
| BLOB | Binary data |

Example:

    id INTEGER
    name TEXT
    marks REAL

---

# 15. NOT NULL

`NOT NULL` prevents a column from containing NULL.

Example:

    name TEXT NOT NULL

This means every student record must have a value for `name`.

---

# 16. UNIQUE

`UNIQUE` prevents duplicate values in a column or set of columns.

Example:

    email TEXT UNIQUE

This is useful when each email address must be different.

---

# 17. DEFAULT

`DEFAULT` provides a value when one is not supplied.

Example:

    status TEXT DEFAULT 'active'

If no status is provided, SQLite uses:

    active

---

# 18. CHECK

`CHECK` enforces a condition.

Example:

    marks INTEGER CHECK (marks >= 0 AND marks <= 100)

This prevents invalid marks from being stored through normal constraint enforcement.

---

# 19. PRIMARY KEY Constraint

Example:

    id INTEGER PRIMARY KEY

This makes `id` the primary key.

SQLite also has special behavior for an `INTEGER PRIMARY KEY`, where it can be associated with the row identifier.

---

# 20. Creating a Table

Example:

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        marks INTEGER CHECK (marks >= 0 AND marks <= 100)
    );

This creates a structured student table.

---

# 21. IF NOT EXISTS

Use `IF NOT EXISTS` when you want table creation to succeed if the table already exists.

Example:

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

---

# 22. Relationships Between Tables

Tables can have different relationships.

Important relationship types:

- One-to-One
- One-to-Many
- Many-to-Many

---

# 23. One-to-One

One record in Table A is associated with one record in Table B.

Example:

    Student
       ↕
    Student Profile

A student can have one profile.

---

# 24. One-to-Many

One record can be related to many records.

Example:

    One Course
       ↓
    Many Students

A course can have many enrolled students.

The foreign key is generally placed on the "many" side.

---

# 25. Many-to-Many

Many records in one table can relate to many records in another table.

Example:

    Students ↔ Courses

One student can take many courses.

One course can have many students.

A junction table is commonly used:

    enrollments

    id
    student_id
    course_id

---

# 26. Junction Table

A junction table represents a many-to-many relationship.

Example:

    students
        ↓
    enrollments
        ↓
    courses

The enrollment table connects students and courses.

---

# 27. Composite Key

A primary key can contain more than one column.

Example:

    PRIMARY KEY (student_id, course_id)

This can be useful in an enrollment table when the same student should not be enrolled in the same course more than once.

---

# 28. Normalization Basics

Normalization is the process of organizing data to reduce unnecessary duplication and improve consistency.

A poorly designed table might contain:

    student_id
    student_name
    course1
    course2
    course3

A better design can separate students and courses and use an enrollment table.

---

# 29. Data Duplication

Consider:

    Student | Course | Instructor
    ------- | ------ | ----------
    Saloni  | Python | Amit
    Rahul   | Python | Amit
    Priya   | Python | Amit

The instructor information is repeated.

A separate course table can reduce this duplication.

---

# 30. NULL

NULL means that a value is missing or unknown.

NULL is different from:

- `0`
- Empty string `''`
- `False`

Example:

    phone TEXT

A student may have no phone value.

---

# 31. Naming Tables and Columns

Use clear and consistent names.

Good:

    students
    student_id
    course_id
    email

Avoid unclear names such as:

    x
    data1
    value2

Good names make SQL easier to understand.

---

# 32. Example Database Design

A student learning application can use:

    students
    ├── id
    ├── name
    └── email

    courses
    ├── id
    ├── name
    └── credits

    enrollments
    ├── student_id
    └── course_id

Relationships:

    students
        ↓
    enrollments
        ↓
    courses

---

# 33. Creating Related Tables

Example:

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        credits INTEGER CHECK (credits > 0)
    );

    CREATE TABLE enrollments (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );

---

# 34. Foreign Key Diagram

Think of:

    students.id
          ↑
          |
    enrollments.student_id


    courses.id
          ↑
          |
    enrollments.course_id

The enrollment table connects the two entities.

---

# 35. Good Database Design Process

A simple process is:

    1. Understand requirements
             ↓
    2. Identify entities
             ↓
    3. Identify attributes
             ↓
    4. Choose primary keys
             ↓
    5. Identify relationships
             ↓
    6. Add foreign keys
             ↓
    7. Add constraints
             ↓
    8. Review duplication
             ↓
    9. Create tables
             ↓
    10. Test with sample data

---

# 36. Common Mistakes

### Mistake 1 — One Giant Table

Putting unrelated information into one table can create duplication.

### Mistake 2 — No Primary Key

Without a reliable way to identify records, data management becomes difficult.

### Mistake 3 — Incorrect Data Types

Choose data types according to the kind of value being stored.

### Mistake 4 — Missing Constraints

Important business rules should be enforced where appropriate.

### Mistake 5 — Incorrect Foreign Keys

Foreign keys should reference appropriate keys.

### Mistake 6 — Repeating Groups

Columns such as:

    course1
    course2
    course3

often indicate that the design should be reconsidered.

---

# 37. Best Practices

- Design tables around entities.
- Use meaningful names.
- Choose appropriate data types.
- Define primary keys.
- Use foreign keys for relationships.
- Add appropriate constraints.
- Avoid unnecessary duplication.
- Use junction tables for many-to-many relationships.
- Keep database rules clear.
- Test the design with realistic sample data.

---

# ⭐ Key Takeaway

Good database design organizes data into meaningful tables and relationships.

The important concepts are:

    Entity
       ↓
    Attributes
       ↓
    Table
       ↓
    Primary Key
       ↓
    Relationships
       ↓
    Foreign Keys
       ↓
    Constraints

A well-designed database provides a strong foundation for Flask applications and future CRUD operations.