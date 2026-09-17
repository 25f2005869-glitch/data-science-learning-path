# 📝 Day 032 — CSS Flexbox Advanced Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 032  
**Topic:** CSS Flexbox Advanced

---

## 🎯 Practice Objectives

- Understand advanced Flexbox properties.
- Practice flexible item sizing.
- Learn growth and shrinking.
- Use `flex` shorthand.
- Control item order.
- Use individual alignment.
- Build responsive card layouts.

---

## Part A — Conceptual Questions

### 1. What is `flex-grow`?

### 2. What is the default value of `flex-grow`?

### 3. What is `flex-shrink`?

### 4. What is the default value of `flex-shrink`?

### 5. What does `flex-basis` define?

### 6. What does the `flex` shorthand represent?

### 7. What is the meaning of:

    flex: 1 1 200px;

### 8. What is the purpose of `order`?

### 9. What is the default value of `order`?

### 10. What does `align-self` do?

---

## Part B — Understand the Properties

### 11. What is the difference between `flex-grow` and `flex-shrink`?

### 12. What is the difference between `flex-basis` and `width`?

### 13. What is the difference between `align-items` and `align-self`?

### 14. Why is `flex: 1` commonly used?

### 15. Why should `order` be used carefully for accessibility?

---

## Part C — Predict the Result

### 16. Consider:

    .container {
        display: flex;
    }

    .item {
        flex-grow: 1;
    }

What happens when multiple items have the same `flex-grow` value?

### 17. Consider:

    .item {
        flex-grow: 2;
    }

How does its growth factor compare with an item having `flex-grow: 1`, assuming other conditions are comparable?

### 18. Consider:

    .item {
        flex-shrink: 0;
    }

What happens when the container becomes too small?

### 19. Consider:

    .item {
        order: -1;
    }

Where does the item generally appear compared with items whose order remains `0`?

### 20. Consider:

    .item {
        align-self: flex-end;
    }

Which axis is affected?

---

## Part D — Write CSS

### 21. Create a flex item that can grow.

### 22. Create a flex item that cannot shrink.

### 23. Give a flex item an initial basis of 250px.

### 24. Write the shorthand equivalent of:

    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 300px;

### 25. Make one flex item appear before the others using `order`.

### 26. Align one flex item to the end of the cross axis.

---

## Part E — Responsive Layout

### 27. Create a responsive card container.

Requirements:

- `display: flex`
- `flex-wrap: wrap`
- `gap: 20px`

### 28. Create a responsive card using:

    flex: 1 1 250px;

### 29. Explain why `flex-wrap: wrap` is useful with flexible cards.

### 30. Create four cards that automatically share available space.

---

## Part F — Debugging

### 31. Find the problem:

    .card {
        flex-grow: 1;
    }

The developer expects the card to have a starting width of 250px. What property is missing?

### 32. Find the problem:

    .special {
        align-items: flex-end;
    }

The developer wants to align only one flex item. Which property should be used?

### 33. Why might `order` create an accessibility problem if the HTML order is not logical?

### 34. Why can `flex-shrink: 0` cause overflow?

### 35. What happens if a flex item has `flex-grow: 0` and extra space is available?

---

## Part G — Mini Challenge

### Project: Responsive Student Course Cards

Create a responsive course-card section.

Required courses:

- DBMS
- PDSA
- MLF
- MAD 1
- BDM

### Requirements

Use:

- `display: flex`
- `flex-wrap`
- `gap`
- `flex-grow`
- `flex-shrink`
- `flex-basis`
- `flex`
- `order`
- `align-self`

### Bonus

Make the cards responsive so that:

- Large screens show multiple cards in a row.
- Smaller screens automatically wrap cards.
- One special card has a different visual order.
- One card has different cross-axis alignment.

---

## ✅ Self-Check

- [ ] I understand `flex-grow`.
- [ ] I understand `flex-shrink`.
- [ ] I understand `flex-basis`.
- [ ] I can use the `flex` shorthand.
- [ ] I understand `order`.
- [ ] I can use `align-self`.
- [ ] I can create responsive cards.
- [ ] I understand flexible space distribution.

---

## 📌 Navigation

⬅️ Previous: Day 031 — Flexbox Basics  
➡️ Next: Day 033 — CSS Grid Basics