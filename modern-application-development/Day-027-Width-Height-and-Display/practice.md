# 📝 Day 027 — CSS Width, Height and Display — Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 027  
**Topic:** CSS Width, Height and Display

---

## 🎯 Practice Objectives

Practice the following concepts:

- `width`
- `height`
- `min-width`
- `max-width`
- `min-height`
- `max-height`
- `auto`
- `display: block`
- `display: inline`
- `display: inline-block`
- `display: none`
- `visibility: hidden`
- `box-sizing`
- Responsive width
- Width and height calculations

---

# 🟢 Part 1 — Basic Questions

### Q1. What does the CSS `width` property control?

Write your answer:

---

### Q2. What does the CSS `height` property control?

Write your answer:

---

### Q3. What is the difference between `min-width` and `max-width`?

Write your answer:

---

### Q4. What is the purpose of `min-height` and `max-height`?

Write your answer:

---

### Q5. What does `width: auto` generally mean?

Write your answer:

---

# 🟡 Part 2 — Display Property

### Q6. What does the `display` property control?

Write your answer:

---

### Q7. What are the main differences between block and inline elements?

Write your answer:

---

### Q8. What is `display: inline-block`?

Write your answer:

---

### Q9. What happens when you use:

    display: none;

Write your answer:

---

### Q10. What happens when you use:

    visibility: hidden;

Write your answer:

---

# 🔵 Part 3 — Predict the Behavior

### Q11. What happens to these elements?

    .box {
        display: block;
        width: 300px;
        height: 150px;
    }

Answer:

---

### Q12. What happens to this element?

    .text {
        display: inline;
        width: 300px;
        height: 150px;
    }

Answer:

---

### Q13. What happens to this element?

    .card {
        display: inline-block;
        width: 300px;
        height: 150px;
    }

Answer:

---

### Q14. Which display value allows elements to appear beside each other while still allowing width and height?

Answer:

---

# 🟠 Part 4 — Width and Height Practice

### Q15. Write CSS for an element with:

- Width: `400px`
- Height: `250px`

Answer:

---

### Q16. Write CSS for an element with:

- Minimum width: `200px`
- Maximum width: `800px`
- Minimum height: `100px`
- Maximum height: `500px`

Answer:

---

### Q17. Create a responsive container with:

- Width: `100%`
- Maximum width: `900px`
- Horizontal centering

Answer:

---

### Q18. Create a responsive image.

Requirements:

- Image should not exceed its container width.
- Height should maintain its natural aspect ratio.

Answer:

---

# 🟣 Part 5 — Box-Sizing Calculation

### Q19. Calculate the total width.

    width: 300px;
    padding-left: 20px;
    padding-right: 20px;
    border-left: 5px solid black;
    border-right: 5px solid black;

Assume:

    box-sizing: content-box;

Total width:

---

### Q20. Calculate the total width.

    width: 300px;
    padding-left: 20px;
    padding-right: 20px;
    border-left: 5px solid black;
    border-right: 5px solid black;

Assume:

    box-sizing: border-box;

Total width:

---

### Q21. What is the main advantage of:

    box-sizing: border-box;

Answer:

---

# 🔴 Part 6 — Visibility Practice

### Q22. Hide an element completely so that it does not occupy layout space.

Write the CSS:

---

### Q23. Hide an element but keep its layout space.

Write the CSS:

---

### Q24. Explain the difference between:

    display: none;

and:

    visibility: hidden;

Answer:

---

# 💻 Part 7 — Coding Practice

## Q25. Create a Fixed Box

Create a box with:

- Width: `300px`
- Height: `200px`
- `display: block`
- Padding: `20px`
- Border: `2px solid black`

HTML:

    <div class="box">
        Fixed Size Box
    </div>

Write the CSS:

---

## Q26. Create Inline-Block Cards

Create three cards.

Requirements:

- `display: inline-block`
- Width: `250px`
- Height: `180px`
- Padding: `20px`
- Border: `2px solid black`

HTML:

    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
    <div class="card">Card 3</div>

Write the CSS:

---

## Q27. Create a Responsive Container

Requirements:

- Width should be `100%`
- Maximum width should be `900px`
- Horizontal margin should be automatic
- Padding should be `20px`
- Use `border-box`

Write the CSS:

---

# 🧩 Part 8 — Challenge Questions

### Q28. Fix the following CSS.

The container causes horizontal scrolling on small screens:

    .container {
        width: 1200px;
    }

Write a better responsive version.

---

### Q29. Fix the following CSS.

The image overflows its parent:

    img {
        width: 1000px;
    }

Write a responsive solution.

---

### Q30. Choose the Correct Display

You need to create three cards that:

- Appear next to each other when enough space is available.
- Have a specific width.
- Have a specific height.

Which `display` value would be suitable?

Answer:

---

# 🚀 Mini Project Challenge

## Student Dashboard Cards

Create a simple Student Dashboard containing three cards:

1. **Education**
2. **Skills**
3. **Learning Goals**

### HTML Structure

    <div class="dashboard">

        <div class="card">
            <h2>Education</h2>
            <p>IIT Madras BS Degree</p>
        </div>

        <div class="card">
            <h2>Skills</h2>
            <p>Python, SQL, HTML, CSS</p>
        </div>

        <div class="card">
            <h2>Learning Goals</h2>
            <p>Modern Application Development</p>
        </div>

    </div>

### CSS Requirements

Use:

- `width`
- `height` or `min-height`
- `max-width`
- `display: inline-block`
- `padding`
- `border`
- `border-radius`
- `margin`
- `box-sizing`

### Bonus

Make the dashboard responsive using:

    width: 100%;
    max-width: 1000px;

---

# ✅ Self-Check

Before completing Day 027, make sure you can:

- [ ] Explain `width`
- [ ] Explain `height`
- [ ] Use `min-width`
- [ ] Use `max-width`
- [ ] Use `min-height`
- [ ] Use `max-height`
- [ ] Explain `auto`
- [ ] Explain block elements
- [ ] Explain inline elements
- [ ] Explain inline-block elements
- [ ] Use `display: none`
- [ ] Use `visibility: hidden`
- [ ] Explain the difference between `display: none` and `visibility: hidden`
- [ ] Use `box-sizing: border-box`
- [ ] Calculate box dimensions
- [ ] Create responsive containers
- [ ] Create inline-block cards

---

## 🎯 Day 027 Goal

Build a strong understanding of **CSS dimensions and display behavior** so that you can control the size, visibility, and basic layout of HTML elements confidently.

---

## 🔗 Navigation

Previous: Day 026 — CSS Margin, Padding and Border

Current: Day 027 — CSS Width, Height and Display

Next: Day 028 — CSS Positioning

---

**Happy Practicing! 🚀**