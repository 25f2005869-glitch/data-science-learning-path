# ⚡ Day 094 — Project Optimization Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 094  
**Topic:** Project Optimization

---

## 🚀 Optimization Areas

| Area | Main Goal |
|---|---|
| Flask | Faster backend |
| Database | Efficient queries |
| SQLAlchemy | Efficient ORM usage |
| Frontend | Faster rendering |
| Images | Smaller resources |
| JavaScript | Fewer unnecessary operations |
| CSS | Cleaner styles |
| Security | Safer application |
| Code | Better maintainability |

---

## 🗄️ Database

- Filter data in the database.
- Select only required data.
- Avoid unnecessary queries.
- Use indexes where appropriate.
- Use pagination for large datasets.
- Use transactions correctly.

Example:

    db.select(Student).where(Student.course == "Data Science")

---

## 🔎 Search

    request.args

Use GET for search/filter forms.

Remember:

    Search → Query Parameters → Database Filter → Results

---

## 📄 Pagination

Instead of:

    Load 10,000 records

Prefer:

    Page 1 → 10 records
    Page 2 → 10 records
    Page 3 → 10 records

---

## ⚡ Caching

    Request
       ↓
    Check Cache
       ↓
    Available? ── Yes → Return Cached Result
       │
       No
       ↓
    Calculate / Query
       ↓
    Store Result
       ↓
    Return Result

---

## 🎨 Frontend Optimization

### HTML

- Semantic structure
- Clean markup
- Accessible forms

### CSS

- Remove unused rules
- Reuse classes
- Avoid excessive specificity

### JavaScript

- Avoid unnecessary DOM updates
- Reuse functions
- Avoid expensive repeated operations

### Images

- Compress
- Resize
- Use appropriate formats
- Use meaningful `alt`

---

## 🔐 Security

Never sacrifice security for performance.

Important:

- Password hashing
- HTTPS
- CSRF protection
- Input validation
- Authorization
- Secure secrets
- Safe error messages

---

## 🛠️ Refactoring

Refactoring:

    Same behavior
          +
    Better internal code

Benefits:

- Readability
- Maintainability
- Reusability
- Fewer bugs

---

## 📊 Measure Before Optimizing

    Measure
       ↓
    Identify bottleneck
       ↓
    Optimize
       ↓
    Test
       ↓
    Measure again

---

## 🚫 Avoid

- Premature optimization
- Unnecessary complexity
- Huge images
- Loading unnecessary data
- Repeated database queries
- Debug mode in production
- Exposing sensitive errors

---

## ⭐ Golden Rule

**Optimize the bottleneck, not everything.**