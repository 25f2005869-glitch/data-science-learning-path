# 📝 Day 033 — CSS Grid Basics Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 033  
**Topic:** CSS Grid Basics

---

## 🎯 Practice Objectives

- Understand CSS Grid.
- Identify grid containers and grid items.
- Create rows and columns.
- Practice `fr` and `repeat()`.
- Create responsive grid layouts.

---

## Part A — Conceptual Questions

### 1. What is CSS Grid?

### 2. Why is Grid called a two-dimensional layout system?

### 3. What is a grid container?

### 4. What is a grid item?

### 5. How do you create a grid container?

### 6. What is a grid row?

### 7. What is a grid column?

### 8. What is a grid cell?

### 9. What is a grid track?

### 10. What is a grid line?

---

## Part B — Grid Properties

### 11. What does `grid-template-columns` do?

### 12. What does `grid-template-rows` do?

### 13. What does the `fr` unit represent?

### 14. What does `repeat()` do?

### 15. What does the `gap` property do?

### 16. What is the difference between `row-gap` and `column-gap`?

### 17. What is the purpose of `minmax()`?

### 18. What does `auto-fit` help with?

### 19. How is Grid different from Flexbox?

### 20. Can Grid and Flexbox be used together?

---

## Part C — Predict the Layout

### 21. How many equal columns are created?

    grid-template-columns: repeat(3, 1fr);

### 22. What does this mean?

    grid-template-columns: 1fr 2fr;

### 23. How many columns are created?

    grid-template-columns: 200px 200px 200px 200px;

### 24. What does this create?

    grid-template-rows: 100px 200px;

### 25. What is the purpose of:

    gap: 20px;

---

## Part D — Write CSS

### 26. Create a two-column Grid.

### 27. Create a three-column Grid with equal columns.

### 28. Create four equal columns using `repeat()`.

### 29. Create a Grid with:

    200px 1fr 1fr

### 30. Create a Grid with a 20px gap.

---

## Part E — Responsive Grid

### 31. Write a responsive card Grid using:

    repeat(auto-fit, minmax(200px, 1fr))

### 32. Why is `minmax()` useful in responsive Grid layouts?

### 33. Why can fixed-width columns create problems on small screens?

### 34. Create a responsive Grid for five course cards.

### 35. Explain what happens when the browser becomes narrower.

---

## Part F — Debugging

### 36. Find the missing property:

    .container {
        grid-template-columns: repeat(3, 1fr);
    }

Why might this not create the expected Grid?

### 37. What is wrong with using very large fixed column widths on a mobile screen?

### 38. A developer wants spacing between Grid items. Which property should they consider?

### 39. Why is Grid often better suited than Flexbox for a layout that requires both rows and columns?

### 40. What is the difference between:

    gap: 20px;

and:

    margin: 20px;

---

## Part G — Mini Challenge

### Project: Student Course Dashboard

Create a course dashboard using CSS Grid.

Required cards:

- DBMS
- PDSA
- MLF
- MAD 1
- BDM
- MLT

### Requirements

Use:

- `display: grid`
- `grid-template-columns`
- `grid-template-rows`
- `fr`
- `repeat()`
- `gap`
- `minmax()`
- `auto-fit`

### Bonus

Make the dashboard responsive so the number of columns automatically changes according to the available screen width.

---

## ✅ Self-Check

- [ ] I understand CSS Grid.
- [ ] I can create a grid container.
- [ ] I understand grid items.
- [ ] I can create rows.
- [ ] I can create columns.
- [ ] I understand `fr`.
- [ ] I can use `repeat()`.
- [ ] I can use `gap`.
- [ ] I understand `minmax()`.
- [ ] I can create a responsive Grid.

---

## 📌 Navigation

⬅️ Previous: Day 032 — Flexbox Advanced  
➡️ Next: Day 034 — CSS Grid Properties