# 📝 Day 039 — Responsive Cards and Layouts Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 039  
**Topic:** Building Responsive Cards and Layouts

---

## 🎯 Practice Objectives

- Build responsive cards.
- Practice CSS Grid.
- Practice Flexbox.
- Understand `minmax()`.
- Understand `auto-fit` and `auto-fill`.
- Create responsive page layouts.

---

## Part A — Conceptual Questions

### 1. What is a card component?

### 2. Why are cards useful in UI design?

### 3. Why is CSS Grid useful for card layouts?

### 4. Why is Flexbox useful inside a card?

### 5. What does `gap` do?

### 6. What does `minmax()` do?

### 7. What does `auto-fit` do?

### 8. What does `auto-fill` do?

### 9. What is the difference between `auto-fit` and `auto-fill`?

### 10. Why should unnecessary fixed card heights be avoided?

---

## Part B — CSS Practice

### 11. Create a basic card with padding, border and rounded corners.

### 12. Create a three-column Grid of cards.

### 13. Create a one-column mobile card layout.

### 14. Change the layout to two columns above 700px.

### 15. Change the layout to three columns above 1000px.

### 16. Create an automatic responsive Grid using:

    repeat(auto-fit, minmax(220px, 1fr))

### 17. Create the same layout using `auto-fill`.

### 18. Create a Flexbox card layout with wrapping.

### 19. Place a button at the bottom of a card using Flexbox.

### 20. Make a card image responsive.

---

## Part C — Predict the Result

### 21. What does this create?

    grid-template-columns: repeat(3, 1fr);

### 22. What does this mean?

    minmax(220px, 1fr)

### 23. What does this create?

    repeat(auto-fit, minmax(220px, 1fr))

### 24. What happens when:

    flex-wrap: wrap;

### 25. Why is this useful?

    max-width: 1100px;

---

## Part D — Debugging

### 26. Find the problem:

    .card {
        width: 500px;
    }

Why can this cause problems on mobile?

### 27. Find the problem:

    .card img {
        width: 1000px;
    }

How should it be improved?

### 28. A card's content is overflowing because the card has a fixed height. What is a better approach?

### 29. A card grid requires ten different Media Queries. What alternative CSS Grid technique could reduce the need for so many breakpoints?

### 30. Cards are touching each other with no spacing. Which Grid or Flexbox property should be considered?

---

## Part E — Layout Challenge

### 31. Create a responsive page with:

- Header
- Navbar
- Sidebar
- Main content
- Footer

### 32. Make the sidebar and content one column on mobile.

### 33. Make the sidebar and content two columns on larger screens.

### 34. Add a responsive project-card Grid inside the main content.

### 35. Make the project cards automatically adapt using `auto-fit` and `minmax()`.

---

## Part F — Mini Project

### Project: Responsive Student Project Dashboard

Create a responsive dashboard containing:

1. Header
2. Navigation
3. Sidebar
4. Course cards
5. Project cards
6. Progress cards
7. Contact section
8. Footer

### Course Cards

Each card should contain:

- Course name
- Short description
- Status

### Project Cards

Each card should contain:

- Project title
- Description
- Technologies
- Project link

### Requirements

Use:

- CSS Grid
- Flexbox
- `gap`
- `minmax()`
- `auto-fit`
- `max-width`
- `%`
- `rem`
- Media Queries
- Responsive images

---

## 📱 Responsive Requirements

### Mobile

- One-column layout
- Full-width cards
- Comfortable spacing
- No horizontal overflow

### Tablet

- Two-column card layout
- Responsive sidebar/content structure

### Desktop

- Multiple card columns
- Sidebar + main content
- Wider container

---

## ♿ Accessibility Checklist

- [ ] Semantic HTML is used.
- [ ] Images have meaningful `alt` text.
- [ ] Links are keyboard accessible.
- [ ] Focus states are visible.
- [ ] Buttons are actual buttons.
- [ ] Navigation is accessible.
- [ ] Content is readable at different widths.

---

## 🧪 Testing Checklist

- [ ] Small mobile
- [ ] Large mobile
- [ ] Tablet
- [ ] Laptop
- [ ] Desktop
- [ ] No horizontal scrolling
- [ ] Images resize correctly
- [ ] Cards resize correctly
- [ ] Text wraps correctly
- [ ] Buttons remain usable

---

## ✅ Self-Check

- [ ] I can create responsive cards.
- [ ] I understand CSS Grid card layouts.
- [ ] I understand Flexbox card layouts.
- [ ] I understand `minmax()`.
- [ ] I understand `auto-fit`.
- [ ] I understand `auto-fill`.
- [ ] I can build responsive page layouts.
- [ ] I can prevent card overflow.
- [ ] I can make images responsive.
- [ ] I can test layouts at different screen sizes.

---

## 📌 Navigation

⬅️ Previous: Day 038 — Building a Responsive Navbar  
➡️ Next: Day 040 — CSS Mini Project