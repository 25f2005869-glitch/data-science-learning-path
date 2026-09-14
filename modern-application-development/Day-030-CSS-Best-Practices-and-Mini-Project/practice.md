# 📝 Day 030 — CSS Best Practices and Mini Project Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 030  
**Topic:** CSS Best Practices and Mini Project

---

## 🎯 Practice Objectives

- Revise CSS concepts from Days 021–029.
- Improve CSS code quality.
- Practice reusable classes.
- Understand maintainability.
- Build a small responsive project.

---

## Part A — Conceptual Questions

### 1. What is a CSS best practice?

### 2. Why should class names be meaningful?

### 3. Why should unnecessary `!important` be avoided?

### 4. What is CSS specificity?

### 5. Which has higher specificity: an ID or a class?

### 6. Why are reusable CSS classes useful?

### 7. What is the purpose of CSS shorthand properties?

### 8. Why is responsive design important?

### 9. What is the difference between `em` and `rem`?

### 10. Why should CSS and HTML responsibilities be separated?

---

## Part B — Identify the Problem

### 11. Identify the problem:

    .box1 {
        padding: 20px;
    }

    .box2 {
        padding: 20px;
    }

How can this CSS be improved?

### 12. Why can excessive use of IDs make CSS harder to maintain?

### 13. Why is this selector difficult to maintain?

    main section article div h3 span {
        color: blue;
    }

### 14. What is wrong with depending only on color to communicate information?

### 15. Why should fixed widths be used carefully in responsive layouts?

---

## Part C — Write CSS

### 16. Create a reusable `.card` class.

Requirements:

- padding
- border
- border-radius
- margin

### 17. Create a responsive container.

Requirements:

- width: 90%
- maximum width: 1000px
- centered horizontally

### 18. Make an image responsive.

### 19. Create a button with:

- padding
- border
- border-radius
- hover effect

### 20. Create a media query for screens below 600px.

---

## Part D — Debugging

### 21. Find the problem:

    .title {
        color: blue !important;
    }

    #title {
        color: red;
    }

How can the CSS be improved without relying on `!important`?

### 22. Improve this repeated CSS:

    .card1 {
        padding: 20px;
    }

    .card2 {
        padding: 20px;
    }

    .card3 {
        padding: 20px;
    }

### 23. Improve this fixed image style:

    img {
        width: 800px;
        height: 500px;
    }

---

## Part E — Mini Project Challenge

### Project: Student Portfolio Landing Page

Create a responsive student portfolio using HTML and CSS.

### Required Sections

1. Header
2. Navigation
3. About Me
4. Skills
5. Education
6. Projects
7. Contact
8. Footer

### Required CSS Concepts

Use:

- Colors
- Backgrounds
- Fonts
- Text styling
- Margin
- Padding
- Border
- Border radius
- Width
- Height
- `max-width`
- CSS units
- Overflow
- Positioning
- Z-index
- Responsive design
- Hover effects
- Reusable classes

---

## 📋 Project Requirements

- Use meaningful class names.
- Avoid unnecessary `!important`.
- Avoid excessive inline CSS.
- Keep CSS organized.
- Use responsive widths.
- Make images responsive.
- Maintain readable text.
- Use consistent spacing.
- Test the page at different screen sizes.

---

## ✅ Self-Check

Before completing Day 030:

- [ ] I understand CSS best practices.
- [ ] I can create reusable classes.
- [ ] I understand specificity.
- [ ] I can avoid unnecessary repetition.
- [ ] I can write responsive CSS.
- [ ] I understand maintainable CSS.
- [ ] I completed the mini project.
- [ ] I tested the project on different screen sizes.

---

## 📌 Navigation

⬅️ Previous: Day 029 — CSS Units and Overflow  
➡️ Next: Day 031 — CSS Flexbox Basics