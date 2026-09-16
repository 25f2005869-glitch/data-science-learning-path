# 📝 Day 029 — CSS Units and Overflow — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 029  
**Topic:** CSS Units and Overflow

---

## 🎯 Practice Objectives

Practice:

- Absolute and relative units
- `px`, `%`, `em`, `rem`
- `vw`, `vh`, `vmin`, `vmax`
- `ch`
- Unitless values
- `overflow`
- `overflow-x`
- `overflow-y`
- `visible`, `hidden`, `scroll`, `auto`
- Text overflow
- Responsive sizing

---

# 🟢 Part 1 — Basic Questions

### Q1. What is a CSS unit?

Write your answer:

---

### Q2. What is the difference between absolute and relative units?

Write your answer:

---

### Q3. Name four absolute CSS units.

Answer:

---

### Q4. Name five relative CSS units.

Answer:

---

### Q5. What does `px` represent?

Answer:

---

# 🔵 Part 2 — CSS Units

### Q6. What does `50%` generally represent when used for an element's width?

Answer:

---

### Q7. What is the main difference between `em` and `rem`?

Answer:

---

### Q8. If the root font size is `16px`, what is:

    2rem

Answer:

---

### Q9. What does `1vw` represent?

Answer:

---

### Q10. What does `1vh` represent?

Answer:

---

### Q11. What is `vmin` based on?

Answer:

---

### Q12. What is `vmax` based on?

Answer:

---

### Q13. What is `ch` commonly useful for?

Answer:

---

# 🟡 Part 3 — Predict the Result

### Q14. If the parent width is `800px`, approximately how wide is this element?

    width: 50%;

Answer:

---

### Q15. If the root font size is `16px`, calculate:

    font-size: 1.5rem;

Answer:

---

### Q16. If the viewport width is `1200px`, what does:

    width: 50vw;

approximately produce?

Answer:

---

### Q17. If the viewport height is `800px`, what does:

    height: 25vh;

approximately produce?

Answer:

---

# 🌊 Part 4 — Overflow

### Q18. What is CSS overflow?

Write your answer:

---

### Q19. What does this do?

    overflow: visible;

Answer:

---

### Q20. What does this do?

    overflow: hidden;

Answer:

---

### Q21. What does this do?

    overflow: scroll;

Answer:

---

### Q22. What does this do?

    overflow: auto;

Answer:

---

### Q23. What is the difference between:

    overflow-x

and:

    overflow-y

Answer:

---

# 🟠 Part 5 — Text Overflow

### Q24. Which property prevents normal text wrapping?

Answer:

---

### Q25. Which property can show `...` when text is truncated?

Answer:

---

### Q26. Write the common CSS combination for single-line text truncation.

Answer:

---

### Q27. Which property can help break a very long word or URL?

Answer:

---

# 🟣 Part 6 — Coding Practice

## Q28. Responsive Container

Create a container with:

- Width: `100%`
- Maximum width: `900px`
- Centered horizontally

Write the CSS:

---

## Q29. Responsive Image

Create CSS that:

- Prevents an image from exceeding its container.
- Preserves the image's aspect ratio.

Write the CSS:

---

## Q30. Scrollable Box

Create a box with:

- Width: `300px`
- Height: `200px`
- `overflow: auto`

Write the CSS:

---

## Q31. Horizontal Scrolling

Create a container that allows horizontal scrolling when required.

Write the CSS:

---

## Q32. Hidden Overflow

Create a box where overflowing content is clipped.

Write the CSS:

---

# 🔴 Part 7 — Debugging

### Q33. Find the Problem

This element may cause horizontal scrolling on small screens:

    .container {
        width: 1200px;
    }

Write a responsive solution.

---

### Q34. Find the Problem

This image may overflow its parent:

    img {
        width: 1000px;
    }

Write a better solution.

---

### Q35. Find the Problem

The following text is creating unwanted horizontal overflow:

    .title {
        white-space: nowrap;
    }

What other properties could be used to handle the overflow?

Answer:

---

# 🧩 Part 8 — Challenge

### Q36. Create a Responsive Card

Requirements:

- Width: `100%`
- Maximum width: `400px`
- Padding: `20px`
- Border: `2px solid`
- Use `box-sizing: border-box`
- Center the card

Write the CSS:

---

### Q37. Create a Text Ellipsis

Create a single-line title that:

- Does not wrap.
- Hides overflowing text.
- Shows an ellipsis.

Write the CSS:

---

### Q38. Create a Scrollable Table Container

Create a container for a wide table that:

- Can scroll horizontally.
- Does not force the entire page to become wider.

Write the CSS:

---

# 🚀 Mini Project Challenge

## Responsive Student Information Card

Create a responsive student card containing:

- Student name
- Programme
- Skills
- Learning goal
- A long description

### CSS Requirements

Use at least:

    %
    rem
    px
    max-width
    overflow
    overflow-wrap

### Bonus

Create a long project title and use:

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

---

# 🧠 Challenge Question

### Q39.

Explain why this is a useful responsive pattern:

    .container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
    }

Write your answer:

---

### Q40.

Explain the difference between:

    overflow: hidden;

and:

    overflow: auto;

Write your answer:

---

# ✅ Self-Check

Before completing Day 029, make sure you can:

- [ ] Explain CSS units
- [ ] Explain absolute units
- [ ] Explain relative units
- [ ] Use `px`
- [ ] Use `%`
- [ ] Use `em`
- [ ] Use `rem`
- [ ] Use `vw`
- [ ] Use `vh`
- [ ] Understand `vmin` and `vmax`
- [ ] Understand `ch`
- [ ] Explain CSS overflow
- [ ] Use `overflow`
- [ ] Use `overflow-x`
- [ ] Use `overflow-y`
- [ ] Use `overflow: hidden`
- [ ] Use `overflow: auto`
- [ ] Handle long text
- [ ] Create responsive containers
- [ ] Create responsive images

---

## 🎯 Day 029 Goal

Build confidence in choosing appropriate **CSS units** and controlling **content overflow** to create flexible and responsive web layouts.

---

## 🔗 Navigation

Previous: Day 028 — CSS Position and Z-Index

Current: Day 029 — CSS Units and Overflow

Next: Day 030 — CSS Flexbox Basics

---

**Happy Practicing! 🚀**