# 📝 Day 091 — Responsive UI Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 091  
**Topic:** Responsive UI  

---

# 🎯 Practice Objectives

Practice converting a desktop-oriented Flask dashboard into a responsive interface that works on mobile, tablet, and desktop screens.

---

# 🟢 Level 1 — Concepts

### Q1. What is responsive UI?

### Q2. Why is responsive design important?

### Q3. What is mobile-first design?

### Q4. What is the purpose of the viewport meta tag?

### Q5. What is a breakpoint?

### Q6. What is the difference between Flexbox and Grid?

### Q7. Why should fixed-width layouts be avoided?

### Q8. Why is `max-width: 100%` useful for images?

---

# 🟡 Level 2 — CSS Practice

### Q9. Create a responsive container.

Requirements:

- Width: 92%
- Maximum width: 1200px
- Center the container

### Q10. Create a responsive card grid.

Requirements:

- One column on small screens
- Multiple columns on larger screens
- Use `minmax()`

### Q11. Create a responsive two-column form.

Requirements:

Desktop:

    Field | Field

Mobile:

    Field
    Field

### Q12. Make an image responsive.

Requirements:

- Never overflow its container.
- Preserve aspect ratio.

---

# 🟠 Level 3 — Dashboard

Create a responsive dashboard containing:

    Header
    Sidebar
    Summary Cards
    Student Table
    Search Form
    CRUD Actions
    Footer

Desktop layout:

    Sidebar | Main Content

Mobile layout:

    Navigation
    Main Content

---

# 🔵 Level 4 — Responsive Search

Create a search/filter interface containing:

    Search
    Course
    Minimum Marks
    Sort
    Search Button

Desktop:

    Search | Course | Marks | Sort | Button

Mobile:

    Search
    Course
    Marks
    Sort
    Button

---

# 🟣 Level 5 — Responsive CRUD

Create responsive CRUD actions:

    View
    Edit
    Delete

Requirements:

- Buttons must remain usable on mobile.
- Delete should use a POST request in the Flask application.
- Important actions should not depend only on hover.

---

# 🔴 Level 6 — Accessibility Challenge

Check your responsive interface for:

    [ ] Semantic HTML
    [ ] Form labels
    [ ] Keyboard navigation
    [ ] Visible focus
    [ ] Readable text
    [ ] Accessible buttons
    [ ] Meaningful alt text
    [ ] Reduced-motion support

---

# ⭐ Final Challenge

Convert the Student Management System from Day 089–090 into a complete responsive application.

Required pages:

    Login
    Dashboard
    Student List
    Add Student
    Edit Student
    Search/Filter
    Profile

Test at:

    Mobile
    Tablet
    Laptop
    Desktop

---

# ✅ Definition of Done

    [ ] Viewport meta tag added
    [ ] Mobile-first layout implemented
    [ ] Responsive navigation works
    [ ] Sidebar adapts
    [ ] Cards are responsive
    [ ] Forms are responsive
    [ ] Tables do not break the page
    [ ] Images are responsive
    [ ] CRUD buttons remain usable
    [ ] Search controls adapt
    [ ] Media queries work
    [ ] Accessibility checked
    [ ] Reduced motion considered
    [ ] Multiple viewport sizes tested