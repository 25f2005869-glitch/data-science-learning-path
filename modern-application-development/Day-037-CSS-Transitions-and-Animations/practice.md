# 📝 Day 037 — CSS Transitions and Animations Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 037  
**Topic:** CSS Transitions and Animations

---

## 🎯 Practice Objectives

- Understand CSS transitions.
- Practice `transform`.
- Create hover effects.
- Understand `@keyframes`.
- Practice CSS animations.
- Learn animation control properties.
- Consider accessibility and reduced motion.

---

## Part A — Conceptual Questions

### 1. What is a CSS transition?

### 2. Why are transitions used?

### 3. What does `transition-duration` control?

### 4. What does `transition-property` control?

### 5. What is a timing function?

### 6. What is `transition-delay`?

### 7. What is the purpose of `transform`?

### 8. What does `translate()` do?

### 9. What does `scale()` do?

### 10. What does `rotate()` do?

---

## Part B — CSS Animation

### 11. What is a CSS animation?

### 12. What is `@keyframes`?

### 13. What does `animation-name` do?

### 14. What does `animation-duration` do?

### 15. What does `animation-iteration-count` do?

### 16. What does `animation-direction` do?

### 17. What does `animation-fill-mode` do?

### 18. What does `animation-play-state` do?

### 19. What is the difference between a transition and an animation?

### 20. When would you use a CSS animation instead of a transition?

---

## Part C — Write CSS

### 21. Create a button that smoothly changes its background color on hover.

### 22. Create a card that moves upward by 5px on hover.

### 23. Create a card that becomes slightly larger on hover.

### 24. Rotate an element by 10 degrees on hover.

### 25. Create a transition for both `transform` and `opacity`.

---

## Part D — Keyframes

### 26. Create a keyframe animation that moves an element from left to right.

### 27. Create a three-stage animation using:

    0%
    50%
    100%

### 28. Create a continuously repeating pulse animation.

### 29. Create an animation that runs three times.

### 30. Create an animation that alternates direction.

---

## Part E — Predict the Result

### 31. What happens here?

    .card {
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: scale(1.1);
    }

### 32. What does this mean?

    animation: pulse 2s ease-in-out infinite;

### 33. What does this do?

    animation-fill-mode: forwards;

### 34. What does this do?

    animation-play-state: paused;

### 35. What is the difference between:

    transform: translateX(20px);

and:

    transform: scale(1.2);

---

## Part F — Debugging

### 36. Find the problem:

    .card:hover {
        transition: transform 0.3s ease;
    }

Why is this not the best place for the transition declaration?

### 37. A developer writes:

    animation: bounce 2s infinite;

but there is no `@keyframes bounce`.

What is missing?

### 38. An animation runs only once but the developer expects it to repeat forever. Which property should be checked?

### 39. A button animation works with mouse hover but keyboard users do not receive the same visual feedback. What should be considered?

### 40. Why should websites consider `prefers-reduced-motion`?

---

## Part G — Mini Challenge

### Project: Animated Student Portfolio

Create a portfolio page with:

1. Header
2. Navigation
3. About section
4. Skills cards
5. Project cards
6. Contact button
7. Footer

### Requirements

Use:

- `transition`
- `transform`
- `:hover`
- `:focus`
- `@keyframes`
- `animation`
- `animation-iteration-count`
- `animation-delay`
- `animation-direction`
- `prefers-reduced-motion`

### Required Effects

- Navigation hover transition
- Button hover effect
- Project card lift effect
- Skill card scale effect
- Animated heading or badge
- Loading/pulse effect

---

## ♿ Accessibility Checklist

- [ ] Keyboard focus is visible.
- [ ] Animations do not block content.
- [ ] Motion is not excessive.
- [ ] Reduced-motion preference is considered.
- [ ] Important information is not communicated only through animation.

---

## ✅ Self-Check

- [ ] I understand transitions.
- [ ] I understand transition timing.
- [ ] I can use `transform`.
- [ ] I can create hover effects.
- [ ] I understand `@keyframes`.
- [ ] I can create CSS animations.
- [ ] I understand animation iteration.
- [ ] I understand animation direction.
- [ ] I understand animation fill mode.
- [ ] I understand reduced-motion preferences.

---

## 📌 Navigation

⬅️ Previous: Day 036 — CSS Media Queries  
➡️ Next: Day 038 — CSS Pseudo-elements and Pseudo-classes