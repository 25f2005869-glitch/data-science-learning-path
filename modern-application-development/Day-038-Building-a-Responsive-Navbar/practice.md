# 📝 Day 038 — Building a Responsive Navbar Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 038  
**Topic:** Building a Responsive Navbar

---

## 🎯 Practice Objectives

- Understand navbar structure.
- Practice semantic navigation.
- Use Flexbox for navigation.
- Build mobile and desktop layouts.
- Practice Media Queries.
- Add accessible hover and focus states.

---

## Part A — Conceptual Questions

### 1. What is a navbar?

### 2. Why is the `<nav>` element used?

### 3. Why can a navigation menu be represented using `<ul>` and `<li>`?

### 4. What is the role of an `<a>` element in navigation?

### 5. Why is Flexbox useful for navbars?

### 6. What does `gap` do in a Flexbox navbar?

### 7. What does `flex-direction: column` do?

### 8. What does `flex-wrap` do?

### 9. What is a responsive navbar?

### 10. What is mobile-first navbar design?

---

## Part B — CSS Practice

### 11. Remove the default bullets from a navigation list.

### 12. Remove the default margin and padding from a navigation list.

### 13. Create a horizontal Flexbox navbar.

### 14. Create a vertical mobile navbar.

### 15. Add 20px spacing between navigation links.

### 16. Center the navigation links horizontally.

### 17. Create a Media Query that changes a vertical navbar to horizontal above 700px.

### 18. Add a hover effect to navigation links.

### 19. Add a visible keyboard focus state.

### 20. Create a sticky navbar.

---

## Part C — HTML Practice

### 21. Create a semantic navigation structure containing:

- Home
- About
- Skills
- Projects
- Contact

### 22. Add an accessible label to the navigation region.

### 23. Use meaningful link text.

### 24. Create a logo link that points to the homepage.

### 25. Create a second navigation region and give it a different accessible label.

---

## Part D — Responsive Design

### 26. Design a mobile-first navbar.

Requirements:

    Mobile → Vertical
    Desktop → Horizontal

### 27. Create a navbar with:

    Logo | Navigation Links

### 28. Make the navbar wrap when there is insufficient horizontal space.

### 29. Prevent navigation content from becoming excessively wide on desktop.

### 30. Explain why a fixed-width navbar can cause horizontal overflow.

---

## Part E — Accessibility

### 31. Why should keyboard users have a visible focus indicator?

### 32. Why should navigation links have meaningful text?

### 33. When should an `<a>` element be used instead of a `<button>`?

### 34. What is the purpose of:

    aria-label="Main navigation"

### 35. Why should navigation links have sufficient clickable area and spacing?

---

## Part F — Debugging

### 36. Find the problem:

    .nav-list {
        display: flex;
        gap: 20px;
    }

The developer expects no bullets, but bullets are still visible. What property is missing?

### 37. A navbar overflows on mobile. List three possible causes.

### 38. A keyboard user cannot see which navigation link has focus. What should be added?

### 39. A developer uses:

    width: 1200px;

for the navbar. Why is this problematic?

### 40. A navigation link is implemented as a button even though it only navigates to another page. Which HTML element is normally more appropriate?

---

## Part G — Mini Challenge

### Project: Responsive Student Portfolio Navbar

Build a responsive navbar for a student portfolio.

### Required Elements

- Logo / Name
- Home
- About
- Education
- Skills
- Projects
- Contact

### Mobile Requirements

- Vertical navigation
- Comfortable spacing
- No horizontal overflow

### Desktop Requirements

- Horizontal navigation
- Centered or distributed links
- Flexible container

### CSS Requirements

Use:

- Flexbox
- `gap`
- `flex-direction`
- `flex-wrap`
- Media Queries
- `:hover`
- `:focus-visible`
- `max-width`
- `width: 90%`

### Accessibility Requirements

- Use `<nav>`.
- Use meaningful link text.
- Provide visible keyboard focus.
- Add an accessible navigation label.

---

## ✅ Testing Checklist

- [ ] Mobile layout works.
- [ ] Tablet layout works.
- [ ] Desktop layout works.
- [ ] Navigation does not overflow.
- [ ] Links are readable.
- [ ] Links are easy to click.
- [ ] Hover state works.
- [ ] Keyboard focus is visible.
- [ ] Navigation is semantically structured.

---

## 📌 Navigation

⬅️ Previous: Day 037 — CSS Transitions and Animations  
➡️ Next: Day 039 — CSS Forms and Responsive Form Design