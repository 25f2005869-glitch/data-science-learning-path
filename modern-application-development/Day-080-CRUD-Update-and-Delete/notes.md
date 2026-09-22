# 📝 Day 080 — CRUD: Update and Delete

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 080  
**Topic:** CRUD: Update and Delete  

---

# 1. CRUD Revision

CRUD stands for:

| Letter | Operation | Purpose |
|---|---|---|
| C | Create | Add records |
| R | Read | Retrieve records |
| U | Update | Modify records |
| D | Delete | Remove records |

Day 079:

    C → Create
    R → Read

Day 080:

    U → Update
    D → Delete

---

# 2. What is Update?

Update means modifying an existing database record.

For example, suppose a student has:

    Name: Saloni
    Course: Mathematics

We want to change the course to:

    Data Science

The existing record is modified rather than creating a new record.

---

# 3. SQL UPDATE vs SQLAlchemy

Raw SQL:

    UPDATE students
    SET course = 'Data Science'
    WHERE id = 1;

SQLAlchemy ORM:

    student = session.get(Student, 1)

    student.course = "Data Science"

    session.commit()

SQLAlchemy tracks the changed object and generates the appropriate SQL when the transaction is committed.

---

# 4. Update Flow

The basic Update flow is:

    Find Record
         ↓
    Modify Object
         ↓
    session.commit()
         ↓
    Database Updated

---

# 5. Find the Record

Usually, the first step is to retrieve the record.

Example:

    student = session.get(Student, 1)

Here:

- `Student` is the model.
- `1` is the primary key.

If the record exists, `student` contains the Student object.

If it does not exist:

    student is None

---

# 6. Check Before Updating

Always consider the possibility that the record does not exist.

Example:

    student = session.get(Student, 1)

    if student is not None:
        student.course = "Data Science"
        session.commit()
    else:
        print("Student not found")

This prevents attempting to modify a missing object.

---

# 7. Updating a Single Attribute

Example:

    student = session.get(Student, 1)

    if student:
        student.name = "Saloni Tiwari"
        session.commit()

The name is changed and committed.

---

# 8. Updating Multiple Attributes

Multiple attributes can be changed before committing.

Example:

    student = session.get(Student, 1)

    if student:
        student.name = "Saloni Tiwari"
        student.age = 18
        student.course = "Data Science"

        session.commit()

All these changes are included in the transaction.

---

# 9. Why Commit is Required

Changing a Python object does not mean the database transaction has been permanently saved.

Example:

    student.name = "New Name"

Then:

    session.commit()

The commit tells SQLAlchemy to persist the changes.

Think:

    Modify Object
         ↓
    Commit
         ↓
    Save Changes

---

# 10. Update with Filtering

You can first find a record using a condition.

Example:

    from sqlalchemy import select

    student = session.scalars(
        select(Student)
        .where(Student.email == "saloni@example.com")
    ).one_or_none()

    if student:
        student.course = "Data Science"
        session.commit()

---

# 11. Updating Several Records

A query can be used to retrieve multiple objects.

Example:

    students = session.scalars(
        select(Student)
        .where(Student.course == "Mathematics")
    ).all()

Then:

    for student in students:
        student.course = "Data Science"

    session.commit()

All matching objects are changed and committed together.

---

# 12. Delete Operation

Delete removes an existing database record.

Raw SQL:

    DELETE FROM students
    WHERE id = 1;

SQLAlchemy:

    student = session.get(Student, 1)

    if student:
        session.delete(student)
        session.commit()

---

# 13. Delete Flow

The basic Delete flow is:

    Find Record
         ↓
    session.delete()
         ↓
    session.commit()
         ↓
    Record Removed

---

# 14. `session.delete()`

`session.delete()` marks an object for deletion.

Example:

    student = session.get(Student, 1)

    session.delete(student)

The deletion is normally sent to the database when the transaction is flushed/committed.

To permanently save the transaction:

    session.commit()

---

# 15. Delete with a Check

Example:

    student = session.get(Student, 5)

    if student:
        session.delete(student)
        session.commit()
    else:
        print("Student not found")

This avoids attempting to delete a record that does not exist.

---

# 16. Delete Multiple Records

First retrieve the records.

    students = session.scalars(
        select(Student)
        .where(Student.age < 18)
    ).all()

Then delete each object.

    for student in students:
        session.delete(student)

    session.commit()

This deletes all matching objects.

---

# 17. Update vs Delete

| Operation | Main Action |
|---|---|
| Update | Modify object attributes |
| Delete | Mark object for deletion |
| Update save | `session.commit()` |
| Delete save | `session.commit()` |

Example Update:

    student.name = "New Name"
    session.commit()

Example Delete:

    session.delete(student)
    session.commit()

---

# 18. Rollback

Suppose an error occurs during a transaction.

Use:

    session.rollback()

Example:

    try:
        student.name = "New Name"
        session.commit()

    except Exception:
        session.rollback()
        raise

Rollback cancels uncommitted changes in the current transaction.

---

# 19. Update Transaction

Example:

    try:
        student = session.get(Student, 1)

        if student:
            student.course = "Data Science"
            session.commit()

    except Exception:
        session.rollback()
        raise

---

# 20. Delete Transaction

Example:

    try:
        student = session.get(Student, 1)

        if student:
            session.delete(student)
            session.commit()

    except Exception:
        session.rollback()
        raise

---

# 21. `session.get()` for Update and Delete

`session.get()` is convenient when the primary key is known.

Update:

    student = session.get(Student, 1)

    if student:
        student.age = 18
        session.commit()

Delete:

    student = session.get(Student, 1)

    if student:
        session.delete(student)
        session.commit()

---

# 22. Update Using `select()`

When the search condition is not the primary key, use a query.

Example:

    statement = select(Student).where(
        Student.email == "saloni@example.com"
    )

    student = session.scalars(
        statement
    ).one_or_none()

Then:

    if student:
        student.course = "Data Science"
        session.commit()

---

# 23. Delete Using a Search Condition

Example:

    statement = select(Student).where(
        Student.email == "old@example.com"
    )

    student = session.scalars(
        statement
    ).one_or_none()

    if student:
        session.delete(student)
        session.commit()

---

# 24. Flask-SQLAlchemy Update

Example:

    student = db.session.get(Student, 1)

    if student:
        student.course = "Data Science"
        db.session.commit()

---

# 25. Flask-SQLAlchemy Delete

Example:

    student = db.session.get(Student, 1)

    if student:
        db.session.delete(student)
        db.session.commit()

---

# 26. Complete CRUD

After Day 079 and Day 080, the complete CRUD flow is:

    CREATE
        ↓
    session.add()
        ↓
    commit()

    READ
        ↓
    select()
        ↓
    scalars()

    UPDATE
        ↓
    Find object
        ↓
    Modify attributes
        ↓
    commit()

    DELETE
        ↓
    Find object
        ↓
    session.delete()
        ↓
    commit()

---

# 27. Example Student Model

    from sqlalchemy import String
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column

    class Base(DeclarativeBase):
        pass

    class Student(Base):
        __tablename__ = "students"

        id: Mapped[int] = mapped_column(
            primary_key=True
        )

        name: Mapped[str] = mapped_column(
            String(100)
        )

        email: Mapped[str] = mapped_column(
            String(120)
        )

        age: Mapped[int]

        course: Mapped[str] = mapped_column(
            String(100)
        )

---

# 28. Complete Update Example

    student = session.get(Student, 1)

    if student is None:
        print("Student not found")
    else:
        student.name = "Saloni Tiwari"
        student.age = 18
        student.course = "Data Science"

        session.commit()

        print("Student updated successfully")

---

# 29. Complete Delete Example

    student = session.get(Student, 2)

    if student is None:
        print("Student not found")
    else:
        session.delete(student)
        session.commit()

        print("Student deleted successfully")

---

# 30. Important Difference: Delete vs Update

Update:

    student.course = "Data Science"

The record remains in the database.

Delete:

    session.delete(student)

The record is removed after the transaction is committed.

---

# 31. Common Mistakes

## Mistake 1 — Forgetting `commit()`

    student.name = "New Name"

Without committing, the change is not persisted as part of a committed transaction.

---

## Mistake 2 — Updating a `None` object

Incorrect:

    student = session.get(Student, 100)
    student.name = "New Name"

If ID 100 does not exist, `student` is `None`.

Better:

    if student:
        student.name = "New Name"

---

## Mistake 3 — Deleting without checking

Always understand which record is being deleted.

---

## Mistake 4 — Deleting the wrong record

Be careful with filtering conditions and IDs.

---

## Mistake 5 — Forgetting rollback after an exception

If a transaction fails:

    session.rollback()

---

## Mistake 6 — Updating every record accidentally

Always verify the query condition before performing bulk changes.

---

# 32. Safety Before Delete

Before deleting an important record:

1. Identify the record.
2. Verify the condition.
3. Check relationships if applicable.
4. Delete the intended object.
5. Commit the transaction.

---

# 33. Best Practices

- Retrieve the record before modifying it.
- Check whether the record exists.
- Commit intentional changes.
- Use rollback after transaction failures.
- Use primary keys when appropriate.
- Carefully construct filtering conditions.
- Avoid accidental bulk updates/deletes.
- Validate user input.
- Use authorization checks in real applications.
- Handle database exceptions.
- Test CRUD operations before deploying.

---

# 34. Key Takeaways

### Update

    object = session.get(Model, id)

    object.field = new_value

    session.commit()

### Delete

    object = session.get(Model, id)

    session.delete(object)

    session.commit()

### Missing Record

    if object is None:
        print("Record not found")

### Failed Transaction

    session.rollback()

---

# ⭐ Final Mental Model

    UPDATE
       │
       ├── Find record
       ├── Modify attributes
       └── Commit


    DELETE
       │
       ├── Find record
       ├── session.delete()
       └── Commit

After Day 080:

    CREATE → READ → UPDATE → DELETE

You now understand the complete basic CRUD lifecycle with SQLAlchemy.