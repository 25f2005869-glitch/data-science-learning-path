# 📝 Day 077 — Database Design and Tables Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 077  
**Topic:** Database Design and Tables

---

# 🎯 Practice Objectives

Practice:

- Database design
- Entities
- Attributes
- Tables
- Primary keys
- Foreign keys
- Constraints
- Relationships
- Normalization basics
- SQLite table creation

---

# 🟢 Level 1 — Basic Questions

### Q1. What is database design?

### Q2. What is a table?

### Q3. What is a row?

### Q4. What is a column?

### Q5. What is an entity?

### Q6. What is an attribute?

### Q7. What is a primary key?

### Q8. What is a foreign key?

---

# 🟡 Level 2 — Constraints

### Q9. What does `NOT NULL` do?

### Q10. What does `UNIQUE` do?

### Q11. What is the purpose of `DEFAULT`?

### Q12. What does a `CHECK` constraint do?

### Q13. Write a column definition for an email that must be unique.

### Q14. Write a marks column that accepts values from 0 to 100.

---

# 🟠 Level 3 — Table Design

### Q15. Design a `students` table.

Required attributes:

- ID
- Name
- Email
- Phone

Choose appropriate data types and constraints.

### Q16. Design a `courses` table.

Required attributes:

- ID
- Course name
- Credits
- Description

### Q17. Explain which column should be the primary key in both tables.

---

# 🟠 Level 4 — Relationships

### Q18. Give an example of a one-to-one relationship.

### Q19. Give an example of a one-to-many relationship.

### Q20. Give an example of a many-to-many relationship.

### Q21. Why is a junction table needed for many-to-many relationships?

### Q22. Design an `enrollments` table connecting:

    students

and:

    courses

---

# 🔵 Level 5 — SQL Practice

### Q23. Create the following table:

    students

Columns:

- `id`
- `name`
- `email`
- `marks`

Requirements:

- `id` is the primary key.
- `name` cannot be NULL.
- `email` must be unique.
- `marks` must be between 0 and 100.

### Q24. Create a `courses` table with:

- `id`
- `name`
- `credits`

Make `credits` greater than zero.

### Q25. Create an `enrollments` table.

Include:

- `student_id`
- `course_id`

Use foreign keys.

---

# 🔴 Level 6 — Database Design Challenge

## Student Learning Database

Design a database for a student learning application.

### Requirements

A student can:

- Have a profile.
- Enroll in multiple courses.
- Have marks for courses.
- View course information.

A course can:

- Have many students.
- Have a name.
- Have credits.
- Have an instructor.

---

## Step 1 — Identify Entities

Identify the required entities.

Possible entities:

    students
    courses
    enrollments

Add other entities if necessary.

---

## Step 2 — Identify Attributes

For each entity, list its attributes.

Example:

    students
    ├── id
    ├── name
    └── email

---

## Step 3 — Identify Primary Keys

Choose the primary key for each table.

---

## Step 4 — Identify Relationships

Determine:

- One-to-one relationships
- One-to-many relationships
- Many-to-many relationships

---

## Step 5 — Add Foreign Keys

Identify which columns should reference other tables.

---

## Step 6 — Add Constraints

Consider:

- `NOT NULL`
- `UNIQUE`
- `DEFAULT`
- `CHECK`
- `PRIMARY KEY`
- `FOREIGN KEY`

---

# 🧪 Testing Checklist

### Tables

- [ ] Students table created.
- [ ] Courses table created.
- [ ] Enrollments table created.

### Keys

- [ ] Primary keys defined.
- [ ] Foreign keys defined.
- [ ] Foreign-key enforcement enabled when needed.

### Constraints

- [ ] Required fields use NOT NULL.
- [ ] Unique fields use UNIQUE.
- [ ] Numeric values use CHECK where appropriate.
- [ ] Default values are used where useful.

### Design

- [ ] No unnecessary repeated columns.
- [ ] Relationships are clear.
- [ ] Table names are meaningful.
- [ ] Column names are meaningful.

---

# 🧠 Revision Questions

1. Why is database design important?
2. What is an entity?
3. What is an attribute?
4. What is the difference between a row and a column?
5. Why do we need a primary key?
6. What is a foreign key?
7. What is referential integrity?
8. What is a one-to-one relationship?
9. What is a one-to-many relationship?
10. What is a many-to-many relationship?
11. What is a junction table?
12. What is a composite primary key?
13. Why use `NOT NULL`?
14. Why use `UNIQUE`?
15. Why use `CHECK`?
16. What is normalization?
17. Why should unnecessary data duplication be avoided?
18. Why should SQLite foreign-key enforcement be enabled when foreign-key constraints are being relied upon?

---

# ⭐ Self-Check

Before moving to Day 078, make sure you can:

- [ ] Explain database design.
- [ ] Identify entities.
- [ ] Identify attributes.
- [ ] Design tables.
- [ ] Define primary keys.
- [ ] Define foreign keys.
- [ ] Use common constraints.
- [ ] Explain table relationships.
- [ ] Design a junction table.
- [ ] Create related SQLite tables.