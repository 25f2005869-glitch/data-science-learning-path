# 📝 Day 035 — Responsive Web Design Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 035  
**Topic:** Responsive Web Design

---

## 🎯 Practice Objectives

- Understand responsive web design.
- Practice media queries.
- Build mobile-friendly layouts.
- Use responsive units.
- Practice responsive Flexbox and Grid.

---

## Part A — Conceptual Questions

### 1. What is Responsive Web Design?

### 2. Why is responsive design important?

### 3. What is the purpose of the viewport meta tag?

### 4. What is a breakpoint?

### 5. What is mobile-first design?

### 6. What is the difference between fixed and flexible layouts?

### 7. Why is `max-width` useful?

### 8. How can an image be made responsive?

### 9. What is a media query?

### 10. What is horizontal overflow?

---

## Part B — CSS Questions

### 11. Write CSS for a responsive container.

Requirements:

- Width: 90%
- Maximum width: 1100px
- Center horizontally

### 12. Write CSS to make an image responsive.

### 13. Write a media query for screens up to 600px.

### 14. Write CSS for a one-column mobile Grid.

### 15. Write CSS to change a Grid to two columns above 700px.

### 16. Write a responsive Flexbox card layout.

### 17. Write a responsive Grid using:

    repeat(auto-fit, minmax(220px, 1fr))

### 18. Which units are useful for responsive typography?

### 19. How can you prevent a table from causing page-wide horizontal overflow?

### 20. How can you prevent unnecessary fixed-width elements from breaking a mobile layout?

---

## Part C — Predict the Result

### 21. What happens with:

    width: 90%;
    max-width: 1000px;

### 22. What does this do?

    max-width: 100%;
    height: auto;

### 23. What happens when:

    flex-wrap: wrap;

is used?

### 24. What does this mean?

    minmax(200px, 1fr)

### 25. What is the purpose of:

    repeat(auto-fit, minmax(200px, 1fr))

---

## Part D — Debugging

### 26. Find the problem:

    .container {
        width: 1200px;
    }

Why can this cause problems on mobile screens?

### 27. Find the problem:

    img {
        width: 1000px;
    }

How can it be improved?

### 28. A page has horizontal scrolling on mobile. List three possible causes.

### 29. A developer uses many media queries for every small screen width. Why can this become difficult to maintain?

### 30. A responsive layout works on desktop but cards overflow on mobile. What should you check?

---

## Part E — Mini Challenge

### Project: Responsive Student Portfolio

Create a responsive student portfolio containing:

1. Header
2. Navigation
3. About section
4. Skills
5. Education
6. Projects
7. Contact form
8. Footer

### Requirements

Use:

- Viewport meta tag
- Flexible widths
- `max-width`
- Responsive images
- Flexbox
- CSS Grid
- Media queries
- `rem`
- `%`
- `fr`
- `minmax()`
- `auto-fit`

### Responsive Requirements

#### Mobile

- One-column content
- Vertical navigation
- Comfortable spacing

#### Tablet

- Two-column card layout

#### Desktop

- Multiple-column card layout
- Wider content area

---

## Part F — Testing Checklist

Test the website at:

- [ ] Small mobile width
- [ ] Large mobile width
- [ ] Tablet width
- [ ] Laptop width
- [ ] Desktop width

Check:

- [ ] No unwanted horizontal scrolling
- [ ] Images fit containers
- [ ] Text remains readable
- [ ] Navigation remains usable
- [ ] Cards resize correctly
- [ ] Forms remain usable
- [ ] Tables do not break the page

---

## ✅ Self-Check

- [ ] I understand responsive web design.
- [ ] I understand the viewport meta tag.
- [ ] I can write media queries.
- [ ] I understand breakpoints.
- [ ] I understand mobile-first design.
- [ ] I can create responsive Flexbox layouts.
- [ ] I can create responsive Grid layouts.
- [ ] I can prevent horizontal overflow.
- [ ] I can make images responsive.
- [ ] I can test a website at different screen sizes.

---

## 📌 Navigation

⬅️ Previous: Day 034 — CSS Grid Advanced  
➡️ Next: Day 036 — CSS Transitions and Animations