# 📝 Day 031 — CSS Flexbox Basics Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 031  
**Topic:** CSS Flexbox Basics

---

## 🎯 Practice Objectives

- Understand the Flexbox layout model.
- Identify flex containers and flex items.
- Practice main-axis and cross-axis alignment.
- Use direction, wrapping and spacing.
- Build simple responsive layouts.

---

## Part A — Conceptual Questions

### 1. What is CSS Flexbox?

### 2. What is a flex container?

### 3. What is a flex item?

### 4. How does an element become a flex container?

### 5. What is the default value of `flex-direction`?

### 6. What is the main axis?

### 7. What is the cross axis?

### 8. What does `justify-content` control?

### 9. What does `align-items` control?

### 10. What is the purpose of `flex-wrap`?

---

## Part B — Properties

### 11. Write the CSS required to create a flex container.

### 12. Write all four common values of `flex-direction`.

### 13. Write five values of `justify-content`.

### 14. Write common values of `align-items`.

### 15. What is the difference between `flex-wrap: nowrap` and `flex-wrap: wrap`?

### 16. What is the purpose of `gap`?

### 17. What is the difference between `row-gap` and `column-gap`?

### 18. What does `flex-flow` represent?

### 19. What is `align-content` used for?

### 20. Why is understanding the main axis important?

---

## Part C — Predict the Layout

### 21. Consider:

    .container {
        display: flex;
        flex-direction: row;
    }

Is the main axis horizontal or vertical?

### 22. Consider:

    .container {
        display: flex;
        flex-direction: column;
    }

What is the main axis?

### 23. Consider:

    .container {
        display: flex;
        justify-content: center;
    }

Where are the items positioned on the main axis?

### 24. Consider:

    .container {
        display: flex;
        align-items: center;
    }

Which axis is being controlled?

### 25. What happens when:

    flex-wrap: wrap;

is applied?

---

## Part D — Write CSS

### 26. Create a navigation bar using Flexbox.

Requirements:

- Horizontal layout
- Centered items
- 20px gap

### 27. Create three cards in one row.

Requirements:

- Flexbox
- 20px gap

### 28. Make the cards wrap on smaller screens.

### 29. Center an element horizontally and vertically.

### 30. Create a column layout using Flexbox.

---

## Part E — Debugging

### 31. Find the problem:

    .container {
        justify-content: center;
    }

Why might the property not produce the expected result?

### 32. Why might `align-content` appear to do nothing when there is only one flex line?

### 33. Fix this layout so items can wrap:

    .container {
        display: flex;
        flex-wrap: nowrap;
    }

### 34. A developer wants to align items along the main axis but uses `align-items`. What should they check?

### 35. A developer uses Flexbox properties on a parent but forgets `display: flex`. What is the problem?

---

## Part F — Mini Challenge

### Project: Flexbox Student Dashboard

Create a student dashboard using Flexbox.

Required sections:

1. Header
2. Navigation
3. Profile
4. Skills
5. Course Cards
6. Project Cards
7. Footer

### Requirements

Use:

- `display: flex`
- `flex-direction`
- `justify-content`
- `align-items`
- `flex-wrap`
- `gap`
- Responsive widths
- Media query

### Bonus

Create a navigation layout that changes from a row to a column on small screens.

---

## ✅ Self-Check

- [ ] I understand Flexbox.
- [ ] I can create a flex container.
- [ ] I can identify flex items.
- [ ] I understand the main axis.
- [ ] I understand the cross axis.
- [ ] I can use `justify-content`.
- [ ] I can use `align-items`.
- [ ] I can use `flex-wrap`.
- [ ] I can use `gap`.
- [ ] I can build a responsive Flexbox layout.

---

## 📌 Navigation

⬅️ Previous: Day 030 — CSS Best Practices and Mini Project  
➡️ Next: Day 032 — Flexbox Properties