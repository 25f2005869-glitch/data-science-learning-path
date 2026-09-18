# 📝 Day 034 — CSS Grid Advanced Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 034  
**Topic:** CSS Grid Advanced

---

## 🎯 Practice Objectives

- Understand Grid lines and tracks.
- Practice manual item placement.
- Use row and column spanning.
- Practice named Grid areas.
- Build responsive Grid layouts.
- Understand Grid alignment.

---

## Part A — Conceptual Questions

### 1. What is a Grid line?

### 2. What is a Grid track?

### 3. What is a Grid cell?

### 4. What does `grid-column` control?

### 5. What does `grid-row` control?

### 6. What is the purpose of `span`?

### 7. What does `grid-area` represent?

### 8. What is `minmax()`?

### 9. What is `auto-fit`?

### 10. What is `auto-fill`?

---

## Part B — Grid Placement

### 11. What does this mean?

    grid-column: 1 / 3;

### 12. How many column tracks does this item occupy?

    grid-column: 2 / 5;

### 13. What does this do?

    grid-row: span 2;

### 14. Write CSS to make an item span three columns.

### 15. Write CSS to make an item span two rows.

### 16. Convert this into the shorthand property:

    grid-column-start: 1;
    grid-column-end: 4;

### 17. Convert this into the shorthand property:

    grid-row-start: 2;
    grid-row-end: 5;

---

## Part C — `grid-area`

### 18. Explain the four values in:

    grid-area: 1 / 2 / 3 / 4;

### 19. Create a Grid layout using named areas:

    header
    sidebar
    main
    footer

### 20. Draw the expected layout for:

    "header header"
    "sidebar main"
    "footer footer"

---

## Part D — Responsive Grid

### 21. Write a responsive Grid using:

    repeat(auto-fit, minmax(220px, 1fr))

### 22. Why is `minmax()` useful?

### 23. What is the difference between `auto-fit` and `auto-fill`?

### 24. Why are responsive Grid layouts better than fixed-width layouts for cards?

### 25. Create six responsive course cards.

---

## Part E — Alignment

### 26. What does `justify-items` control?

### 27. What does `align-items` control?

### 28. What does `place-items` do?

### 29. What is the difference between `justify-items` and `justify-content`?

### 30. What is the difference between `align-items` and `align-content`?

### 31. Write CSS to center all Grid items inside their cells.

---

## Part F — Debugging

### 32. Find the problem:

    .item {
        grid-column: 1 / 4;
    }

The developer says the item occupies three columns. Explain why the result is actually two tracks.

### 33. Why might this not work?

    .item {
        grid-column: span 2;
    }

What should you check?

### 34. Identify the value order:

    grid-area: 1 / 2 / 4 / 5;

### 35. Why should very large fixed Grid widths be avoided in responsive layouts?

---

## Part G — Mini Challenge

### Project: Student Dashboard

Build a dashboard using CSS Grid.

Required areas:

- Header
- Sidebar
- Main Content
- Course Cards
- Project Cards
- Footer

### Requirements

Use:

- `grid-template-columns`
- `grid-template-rows`
- `grid-column`
- `grid-row`
- `grid-area`
- `span`
- `minmax()`
- `auto-fit`
- `gap`
- `place-items`

### Bonus

Create a featured course card that spans two columns and a project card that spans two rows.

---

## ✅ Self-Check

- [ ] I understand Grid lines.
- [ ] I understand Grid tracks.
- [ ] I can use `grid-column`.
- [ ] I can use `grid-row`.
- [ ] I can use `span`.
- [ ] I understand `grid-area`.
- [ ] I can create named Grid areas.
- [ ] I understand `minmax()`.
- [ ] I understand `auto-fit`.
- [ ] I can create responsive Grid layouts.
- [ ] I understand Grid alignment.

---

## 📌 Navigation

⬅️ Previous: Day 033 — CSS Grid Basics  
➡️ Next: Day 035 — CSS Grid Layout Project