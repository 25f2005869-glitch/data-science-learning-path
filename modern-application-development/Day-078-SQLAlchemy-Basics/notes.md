# 📝 Day 078 — SQLAlchemy Basics

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 078  
**Topic:** SQLAlchemy Basics  

---

## 1. What is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM).

It allows Python applications to communicate with relational databases.

Common databases that can be used with SQLAlchemy include:

- SQLite
- PostgreSQL
- MySQL
- MariaDB
- Oracle

---

## 2. What is ORM?

ORM stands for **Object Relational Mapping**.

ORM connects programming-language objects with database tables.

For example:

Python class:

    class Student:
        name
        email
        age

Database table:

    students
    -------------------------
    id | name | email | age
    -------------------------

The class represents the table, while an object represents a row.

---

## 3. Raw SQL vs ORM

With raw SQL:

    INSERT INTO students (name, email)
    VALUES ('Saloni', 'saloni@example.com');

With SQLAlchemy ORM:

    student = Student(
        name="Saloni",
        email="saloni@example.com"
    )

    db.session.add(student)
    db.session.commit()

ORM allows database operations to be expressed using Python objects.

---

## 4. Installing SQLAlchemy

Install SQLAlchemy using pip:

    pip install sqlalchemy

For Flask applications, Flask-SQLAlchemy can also be used:

    pip install flask-sqlalchemy

Check installation:

    python -c "import sqlalchemy; print(sqlalchemy.__version__)"

---

## 5. SQLAlchemy Engine

The Engine is responsible for communicating with the database.

Example:

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///students.db")

For SQLite:

    sqlite:///students.db

means that `students.db` is a SQLite database file.

---

## 6. Database URI

A database URI tells SQLAlchemy which database to use.

Examples:

    sqlite:///students.db

    postgresql://username:password@localhost/database

    mysql+pymysql://username:password@localhost/database

For MAD 1 practice, SQLite is simple and convenient.

---

## 7. Declarative Models

A model is a Python class representing a database table.

Example:

    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy import String
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column

    class Base(DeclarativeBase):
        pass

    class Student(Base):
        __tablename__ = "students"

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(100))
        email: Mapped[str] = mapped_column(String(120), unique=True)

Here:

- `Student` is the Python model.
- `students` is the database table.
- `id` is the primary key.
- `name` and `email` are columns.

---

## 8. Columns

A database table consists of columns.

Example:

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    age: Mapped[int]

Common SQLAlchemy types include:

- Integer
- String
- Text
- Float
- Boolean
- Date
- DateTime

---

## 9. Primary Key

A primary key uniquely identifies each row.

Example:

    id: Mapped[int] = mapped_column(primary_key=True)

The database can automatically generate integer primary-key values.

Example records:

    1 | Saloni | saloni@example.com
    2 | Rahul  | rahul@example.com

The `id` distinguishes the records.

---

## 10. Creating Tables

After defining the model, tables can be created using:

    Base.metadata.create_all(engine)

This creates tables that do not already exist.

It does not normally recreate existing tables every time the application runs.

---

## 11. Session

A Session manages interaction with the database.

Example:

    from sqlalchemy.orm import Session

    with Session(engine) as session:
        ...

A session can be used to:

- Add objects
- Query objects
- Update objects
- Delete objects
- Commit transactions
- Roll back changes

---

## 12. Adding a Record

Create an object:

    student = Student(
        name="Saloni",
        email="saloni@example.com"
    )

Add it to the session:

    session.add(student)

Save the transaction:

    session.commit()

---

## 13. Adding Multiple Records

Use `add_all()`:

    students = [
        Student(name="Saloni", email="saloni@example.com"),
        Student(name="Rahul", email="rahul@example.com")
    ]

    session.add_all(students)
    session.commit()

---

## 14. Querying Records

SQLAlchemy provides a `select()` construct.

Example:

    from sqlalchemy import select

    statement = select(Student)

    students = session.scalars(statement).all()

This retrieves Student objects.

---

## 15. Filtering Records

Use `where()`:

    statement = select(Student).where(
        Student.name == "Saloni"
    )

    student = session.scalars(statement).first()

This searches for students whose name is Saloni.

---

## 16. Updating Records

First retrieve an object:

    student = session.get(Student, 1)

Then modify it:

    student.name = "Saloni Tiwari"

Save the change:

    session.commit()

The ORM tracks the changed object.

---

## 17. Deleting Records

Retrieve the object:

    student = session.get(Student, 1)

Delete it:

    session.delete(student)

Save:

    session.commit()

---

## 18. Rollback

If something goes wrong before committing:

    session.rollback()

Rollback cancels uncommitted database changes in the current transaction.

---

## 19. Transactions

A transaction is a group of database operations treated as one unit.

Typical workflow:

    session.add(student)
    session.commit()

If an error occurs:

    session.rollback()

Commit saves changes.

Rollback cancels uncommitted changes.

---

## 20. SQLAlchemy with Flask

A Flask application can use Flask-SQLAlchemy.

Basic setup:

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

    db = SQLAlchemy(app)

A model can then be defined using:

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(120), unique=True)

Tables can be created inside an application context:

    with app.app_context():
        db.create_all()

---

## 21. SQLAlchemy CRUD Mapping

| Operation | SQL | SQLAlchemy ORM |
|---|---|---|
| Create | INSERT | `session.add()` |
| Read | SELECT | `select()` |
| Update | UPDATE | Modify object |
| Delete | DELETE | `session.delete()` |

---

## 22. Basic Relationships

SQLAlchemy can represent relationships between models.

Example:

    Student → Course

A student may enroll in many courses.

Relationships are commonly implemented using:

- `relationship()`
- `ForeignKey`

Example concept:

    class Student(Base):
        ...

    class Course(Base):
        ...

Relationships will be studied more deeply in later database topics.

---

## 23. SQLAlchemy vs sqlite3

### sqlite3

Python's built-in SQLite module.

Advantages:

- Simple
- No additional package
- Direct SQL control

Example:

    cursor.execute(
        "SELECT * FROM students"
    )

### SQLAlchemy

Advantages:

- ORM support
- Python objects represent records
- Cleaner application-level database code
- Supports multiple database systems
- Useful for larger applications

---

## 24. Important Concepts

Remember this flow:

    Python Model
          ↓
    SQLAlchemy ORM
          ↓
       Engine
          ↓
      Database
          ↓
        Table
          ↓
        Rows

---

## 25. Common Mistakes

### Mistake 1: Forgetting commit

    session.add(student)

Without:

    session.commit()

the change may not be permanently saved.

### Mistake 2: Using incorrect database URI

Check the URI carefully.

### Mistake 3: Forgetting the primary key

Most ORM models should have a clear primary key.

### Mistake 4: Ignoring rollback

Handle failed transactions appropriately.

### Mistake 5: Storing secrets in source code

Database passwords and secret keys should be stored securely.

---

## 26. Best Practices

- Use meaningful model names.
- Use clear column names.
- Define primary keys.
- Use appropriate data types.
- Use constraints where necessary.
- Keep database configuration separate from application logic.
- Use environment variables for sensitive configuration.
- Commit intentional changes.
- Roll back failed transactions.
- Avoid unnecessary raw SQL.
- Understand the SQL generated by your ORM.
- Validate user input before storing it.

---

## 27. Key Takeaway

SQLAlchemy allows Python applications to work with relational databases using models and objects.

The most important concepts are:

    Engine
    Model
    Column
    Primary Key
    Session
    Add
    Select
    Commit
    Rollback
    Delete
    ORM

These concepts form the foundation for using SQLAlchemy in Flask applications.