# 📝 Day 028 — CSS Position and Z-Index — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 028  
**Topic:** CSS Position and Z-Index

---

## 🎯 Practice Objectives

Practice the following concepts:

- `position`
- `static`
- `relative`
- `absolute`
- `fixed`
- `sticky`
- `top`
- `right`
- `bottom`
- `left`
- Normal document flow
- Containing block
- `z-index`
- Stacking order
- Stacking context
- Overlapping elements
- Practical positioning patterns

---

# 🟢 Part 1 — Basic Questions

### Q1. What is the purpose of the CSS `position` property?

Write your answer:

---

### Q2. What is the default value of the `position` property?

Write your answer:

---

### Q3. What is normal document flow?

Write your answer:

---

### Q4. What happens when an element has:

    position: relative;

Write your answer:

---

### Q5. What happens when an element has:

    position: absolute;

Write your answer:

---

### Q6. What is the main difference between `relative` and `absolute` positioning?

Write your answer:

---

# 🟡 Part 2 — Position Types

### Q7. Match each position value with its main behavior.

    A. static
    B. relative
    C. absolute
    D. fixed
    E. sticky

    1. Default positioning
    2. Remains in flow and can be offset
    3. Removed from flow and positioned relative to a containing block
    4. Positioned relative to the viewport in typical cases
    5. Sticks after reaching a scroll threshold

Answer:

    A →
    B →
    C →
    D →
    E →

---

### Q8. Which position value should generally be used when you want an element to remain in the normal flow but move visually?

Answer:

---

### Q9. Which position value is commonly used for a badge inside a card?

Answer:

---

### Q10. Which position value is commonly used for a floating button attached to the viewport?

Answer:

---

### Q11. Which position value is commonly used for a sticky navigation bar?

Answer:

---

# 🔵 Part 3 — Offset Properties

### Q12. Name the four main offset properties used with positioned elements.

Answer:

---

### Q13. What does this code do?

    .box {
        position: relative;
        top: 20px;
    }

Answer:

---

### Q14. What does this code do?

    .box {
        position: absolute;
        right: 20px;
    }

Answer:

---

### Q15. What does this code do?

    .button {
        position: fixed;
        bottom: 20px;
    }

Answer:

---

# 🟠 Part 4 — Parent and Child Positioning

### Q16. Why is the following pattern commonly used?

    .parent {
        position: relative;
    }

    .child {
        position: absolute;
        top: 10px;
        right: 10px;
    }

Answer:

---

### Q17. What is a containing block?

Write your answer:

---

### Q18. Create a card with a badge positioned at its top-right corner.

HTML:

    <div class="card">
        <span class="badge">New</span>
        <h2>CSS Course</h2>
    </div>

Write the CSS:

---

# 🟣 Part 5 — Z-Index

### Q19. What is the purpose of `z-index`?

Write your answer:

---

### Q20. Which element generally appears above the other when they overlap in the same stacking context?

    .box1 {
        position: absolute;
        z-index: 1;
    }

    .box2 {
        position: absolute;
        z-index: 5;
    }

Answer:

---

### Q21. Arrange these from bottom to top.

    z-index: 1;
    z-index: 10;
    z-index: 5;

Answer:

---

### Q22. Can `z-index` have a negative value?

Answer:

---

### Q23. Why does a very large value such as this not automatically guarantee that an element will appear above everything?

    z-index: 999999;

Answer:

---

# 🔴 Part 6 — Predict the Behavior

### Q24. What happens to the following element?

    .box {
        position: static;
        top: 30px;
        left: 20px;
    }

Answer:

---

### Q25. Does the original layout space remain when using:

    position: relative;

Answer:

---

### Q26. Does the original layout space remain when using:

    position: absolute;

Answer:

---

### Q27. Does an element with `position: fixed` normally remain in the same viewport position while scrolling?

Answer:

---

### Q28. What happens when an element uses:

    position: sticky;
    top: 0;

Answer:

---

# 💻 Part 7 — Coding Practice

## Q29. Relative Positioning

Create a box that:

- Uses `position: relative`
- Moves 20px downward
- Moves 30px to the right

Write the CSS:

---

## Q30. Absolute Positioning

Create a child element positioned:

- 10px from the top
- 10px from the right

Parent:

    .parent {
        position: relative;
    }

Write the child CSS:

---

## Q31. Fixed Button

Create a floating button that remains:

- 20px from the right
- 20px from the bottom

Write the CSS:

---

## Q32. Sticky Header

Create a header that:

- Uses sticky positioning
- Sticks to the top
- Has a suitable `z-index`

Write the CSS:

---

# 🧩 Part 8 — Z-Index Challenge

## Q33. Create Two Overlapping Boxes

Create two boxes that overlap.

Requirements:

- Both should use positioning.
- First box: `z-index: 1`
- Second box: `z-index: 2`
- Second box should appear above the first.

Write the HTML and CSS:

---

## Q34. Three-Layer Challenge

Create three overlapping elements:

    Background
    Middle
    Foreground

Use:

    z-index: 1;
    z-index: 2;
    z-index: 3;

Make the foreground element appear above the other two.

Write the CSS:

---

# 🚀 Mini Project Challenge

## Student Portfolio Positioning Demo

Create a small portfolio card using CSS positioning.

### Requirements

The page should contain:

1. A sticky header
2. A profile card
3. A "New" badge positioned inside the card
4. A profile image
5. A floating button
6. At least two overlapping elements
7. Appropriate `z-index` values

### Suggested Structure

    <header class="header">
        <h1>Student Portfolio</h1>
    </header>

    <main>
        <div class="profile-card">
            <span class="badge">Student</span>

            <h2>Saloni Tiwari</h2>
            <p>IIT Madras BS Degree — Diploma Level</p>
        </div>
    </main>

    <button class="floating-button">
        Top
    </button>

### CSS Requirements

Use:

- `position: sticky`
- `position: relative`
- `position: absolute`
- `position: fixed`
- `top`
- `right`
- `bottom`
- `left`
- `z-index`

---

# 🧠 Challenge Question

### Q35.

You have:

    .card {
        position: relative;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 10;
    }

Explain why `position: relative` is useful on `.card`.

Write your answer:

---

# ⚠️ Debugging Practice

### Q36. Find the Problem

The developer wants the badge to appear inside the card, but it appears in an unexpected location.

    .card {
        width: 300px;
        height: 200px;
    }

    .badge {
        position: absolute;
        top: 10px;
        right: 10px;
    }

What property could be added to `.card` to establish the intended positioning context?

Answer:

---

### Q37. Find the Problem

The developer wants to move a box 20px downward:

    .box {
        position: static;
        top: 20px;
    }

Why does it not move?

How can it be fixed?

---

# ✅ Self-Check

Before completing Day 028, make sure you can:

- [ ] Explain normal document flow
- [ ] Explain `position: static`
- [ ] Explain `position: relative`
- [ ] Explain `position: absolute`
- [ ] Explain `position: fixed`
- [ ] Explain `position: sticky`
- [ ] Use `top`
- [ ] Use `right`
- [ ] Use `bottom`
- [ ] Use `left`
- [ ] Explain a containing block
- [ ] Position a child inside a parent
- [ ] Create a floating button
- [ ] Create a sticky header
- [ ] Create overlapping elements
- [ ] Use `z-index`
- [ ] Understand stacking order
- [ ] Understand basic stacking contexts
- [ ] Debug common positioning problems

---

## 🎯 Day 028 Goal

Build a strong understanding of **CSS positioning and stacking order** so that you can control the location of elements and manage overlapping components confidently.

---

## 🔗 Navigation

Previous: Day 027 — CSS Width, Height and Display

Current: Day 028 — CSS Position and Z-Index

Next: Day 029 — CSS Flexbox

---

**Happy Practicing! 🚀**