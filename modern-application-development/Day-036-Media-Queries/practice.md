# 📝 Day 036 — CSS Media Queries Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 036  
**Topic:** CSS Media Queries

---

## 🎯 Practice Objectives

- Understand Media Queries.
- Practice `min-width` and `max-width`.
- Create responsive breakpoints.
- Practice mobile-first design.
- Combine Media Queries with Flexbox and Grid.

---

## Part A — Conceptual Questions

### 1. What is a CSS Media Query?

### 2. Why are Media Queries used?

### 3. What does `max-width` mean?

### 4. What does `min-width` mean?

### 5. What is a breakpoint?

### 6. What is mobile-first design?

### 7. What is desktop-first design?

### 8. What is the purpose of the `orientation` condition?

### 9. What is the difference between `screen` and `print` media?

### 10. Why should breakpoints be based on content rather than device names?

---

## Part B — Write Media Queries

### 11. Write a Media Query for screens up to 600px.

### 12. Write a Media Query for screens at least 700px wide.

### 13. Write a Media Query for portrait orientation.

### 14. Write a Media Query for landscape orientation.

### 15. Write a Media Query for print.

---

## Part C — Predict the Result

### 16. When does this rule apply?

    @media (max-width: 600px) {
        ...
    }

### 17. When does this rule apply?

    @media (min-width: 800px) {
        ...
    }

### 18. What happens when:

    @media (min-width: 700px) and (max-width: 1000px) {
        ...
    }

### 19. What does this do?

    @media print {
        .navigation {
            display: none;
        }
    }

### 20. Why can a Media Query stop applying when the viewport becomes wider or narrower?

---

## Part D — Responsive Layout

### 21. Create a mobile-first layout with one Grid column.

### 22. Add a Media Query that changes it to two columns above 700px.

### 23. Add another Media Query that changes it to three columns above 1000px.

### 24. Create a navigation that is vertical on mobile and horizontal on larger screens.

### 25. Create a responsive card layout using Flexbox.

---

## Part E — Debugging

### 26. Find the problem:

    @media max-width: 600px {
        ...
    }

What is missing?

### 27. A developer uses:

    @media (min-width: 1200px) {
        .card {
            width: 100%;
        }
    }

but expects the rule to work on small screens. What is wrong?

### 28. Why can too many Media Queries make CSS difficult to maintain?

### 29. A page works at 600px and 1200px but breaks at 850px. What should be checked?

### 30. Why should you test intermediate viewport sizes?

---

## Part F — Mini Challenge

### Project: Responsive Student Dashboard

Create a responsive student dashboard.

Required sections:

1. Header
2. Navigation
3. Sidebar
4. Main Content
5. Course Cards
6. Projects
7. Footer

### Mobile

- One-column layout
- Vertical navigation
- Full-width cards

### Tablet

- Two-column content
- Improved spacing

### Desktop

- Sidebar + main content
- Multiple course columns
- Horizontal navigation

---

## Part G — Requirements

Use:

- `@media`
- `min-width`
- `max-width`
- `min-height`
- `orientation`
- Flexbox
- Grid
- `%`
- `rem`
- `fr`
- `minmax()`

---

## ✅ Self-Check

- [ ] I understand Media Queries.
- [ ] I can use `max-width`.
- [ ] I can use `min-width`.
- [ ] I understand breakpoints.
- [ ] I understand mobile-first design.
- [ ] I can create responsive navigation.
- [ ] I can create responsive Grid layouts.
- [ ] I can create responsive Flexbox layouts.
- [ ] I understand orientation queries.
- [ ] I can test different viewport sizes.

---

## 📌 Navigation

⬅️ Previous: Day 035 — Responsive Web Design  
➡️ Next: Day 037 — CSS Transitions and Animations