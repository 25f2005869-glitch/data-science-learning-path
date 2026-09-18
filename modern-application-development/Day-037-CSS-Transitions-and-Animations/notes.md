# 📚 Day 037 — CSS Transitions and Animations Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 037  
**Topic:** CSS Transitions and Animations

---

## 1. What are CSS Transitions?

A CSS transition creates a smooth change between two states of an element.

For example, a button can smoothly change its background, size or position when the user moves the pointer over it.

Example:

    .button {
        transition: background-color 0.3s ease;
    }

---

## 2. Why Use Transitions?

Transitions make interfaces feel smoother and more interactive.

Common uses:

- Button hover effects
- Navigation effects
- Card interactions
- Form focus effects
- Image effects
- Menu interactions

---

## 3. Basic Transition Syntax

Example:

    .button {
        transition: background-color 0.3s ease;
    }

The main parts are:

    property
    duration
    timing function

---

## 4. `transition-property`

Defines which CSS property should transition.

Example:

    transition-property: background-color;

Multiple properties can be specified:

    transition-property: background-color, transform;

You can also use:

    transition-property: all;

However, transitioning only the properties that need animation is generally clearer and can avoid unnecessary work.

---

## 5. `transition-duration`

Defines how long the transition takes.

Example:

    transition-duration: 0.3s;

Other units such as milliseconds can also be used:

    transition-duration: 300ms;

Remember:

    1s = 1000ms

---

## 6. `transition-timing-function`

Controls the speed pattern of the transition.

Common values:

    linear
    ease
    ease-in
    ease-out
    ease-in-out

Example:

    transition-timing-function: ease-in-out;

---

## 7. Timing Functions

### `linear`

The transition progresses at a constant rate.

### `ease`

Starts and ends more gradually.

### `ease-in`

Starts slowly and becomes faster.

### `ease-out`

Starts faster and slows down toward the end.

### `ease-in-out`

Starts slowly, speeds up, then slows down.

---

## 8. `transition-delay`

Defines how long the browser waits before starting the transition.

Example:

    transition-delay: 0.2s;

---

## 9. Transition Shorthand

Instead of:

    transition-property: transform;
    transition-duration: 0.4s;
    transition-timing-function: ease;
    transition-delay: 0s;

Use:

    transition: transform 0.4s ease;

General syntax:

    transition: property duration timing-function delay;

---

## 10. Multiple Transitions

Example:

    transition:
        background-color 0.3s ease,
        transform 0.3s ease;

Different properties can have different transition settings.

---

## 11. Transitions Need a State Change

A transition normally occurs when a CSS property changes between states.

Common trigger:

    :hover

Example:

    .card:hover {
        transform: scale(1.03);
    }

The transition should normally be placed on the base element:

    .card {
        transition: transform 0.3s ease;
    }

---

## 12. CSS `transform`

`transform` changes the visual geometry of an element without changing the normal document flow in the same way as layout properties.

Common functions include:

    translate()
    translateX()
    translateY()
    scale()
    rotate()
    skew()

---

## 13. `translate()`

Moves an element visually.

Example:

    transform: translate(20px, 10px);

The first value affects the horizontal direction and the second affects the vertical direction.

---

## 14. `translateX()`

Moves an element horizontally.

Example:

    transform: translateX(20px);

---

## 15. `translateY()`

Moves an element vertically.

Example:

    transform: translateY(-10px);

---

## 16. `scale()`

Changes the visual size of an element.

Example:

    transform: scale(1.1);

This makes the element appear 10% larger.

---

## 17. `rotate()`

Rotates an element.

Example:

    transform: rotate(5deg);

---

## 18. Combining Transforms

Multiple transform functions can be combined.

Example:

    transform: translateY(-5px) scale(1.03) rotate(1deg);

The order of transform functions can affect the result.

---

## 19. Transition and Transform Together

A common UI pattern is:

    .card {
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

The card smoothly moves upward when hovered.

---

## 20. CSS Animations

A CSS animation can perform a sequence of style changes automatically.

Unlike a basic transition, an animation can have multiple stages.

CSS animations are commonly created using:

    @keyframes

---

## 21. `@keyframes`

`@keyframes` defines the stages of an animation.

Example:

    @keyframes slide {
        from {
            transform: translateX(0);
        }

        to {
            transform: translateX(100px);
        }
    }

---

## 22. Percentage Keyframes

Animations can use percentages.

Example:

    @keyframes example {
        0% {
            transform: translateX(0);
        }

        50% {
            transform: translateX(100px);
        }

        100% {
            transform: translateX(0);
        }
    }

This allows multiple animation stages.

---

## 23. `animation-name`

Specifies the name of the keyframe animation.

Example:

    animation-name: slide;

The name must match a defined `@keyframes` rule.

---

## 24. `animation-duration`

Defines how long one animation cycle takes.

Example:

    animation-duration: 2s;

---

## 25. `animation-timing-function`

Controls the speed pattern of an animation.

Example:

    animation-timing-function: ease-in-out;

---

## 26. `animation-delay`

Delays the beginning of an animation.

Example:

    animation-delay: 1s;

---

## 27. `animation-iteration-count`

Defines how many times the animation runs.

Example:

    animation-iteration-count: 3;

For continuous repetition:

    animation-iteration-count: infinite;

---

## 28. `animation-direction`

Controls the direction of animation cycles.

Common values:

    normal
    reverse
    alternate
    alternate-reverse

Example:

    animation-direction: alternate;

---

## 29. `animation-fill-mode`

Controls styles before and/or after the animation.

Common values:

    none
    forwards
    backwards
    both

Example:

    animation-fill-mode: forwards;

`forwards` keeps the styles from the final keyframe after the animation finishes.

---

## 30. `animation-play-state`

Controls whether an animation is running or paused.

Values:

    running
    paused

Example:

    animation-play-state: paused;

This can be useful for hover-controlled animations.

---

## 31. Animation Shorthand

Instead of writing several animation properties separately:

    animation-name: pulse;
    animation-duration: 2s;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;

You can use:

    animation: pulse 2s ease-in-out infinite;

---

## 32. Transition vs Animation

### Transition

Usually changes smoothly between two states.

Example:

    normal → hover

### Animation

Can have multiple stages and can run automatically.

Example:

    0% → 50% → 100%

---

## 33. Transition vs Animation Table

| Feature | Transition | Animation |
|---|---|---|
| Main purpose | State change | Multi-step motion |
| Trigger | Usually a state change | Can start automatically |
| Keyframes | Not required | Required for custom keyframe sequences |
| Multiple stages | Limited | Yes |
| Looping | No built-in iteration count | Yes |
| Common use | Hover effects | Loading, movement, attention effects |

---

## 34. Animatable Properties

Many CSS properties can be animated or transitioned.

Common examples:

    opacity
    transform
    color
    background-color
    width
    height
    margin
    padding

For smooth performance, `transform` and `opacity` are often preferred for many visual effects.

---

## 35. Opacity

`opacity` controls visual transparency.

Example:

    opacity: 0.5;

Values generally range from:

    0 → Fully transparent
    1 → Fully opaque

Example transition:

    .image {
        transition: opacity 0.3s ease;
    }

    .image:hover {
        opacity: 0.7;
    }

---

## 36. Hover Animation

Example:

    .card {
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-8px);
    }

This creates a simple hover effect.

---

## 37. Focus Effects

Animations should not be limited to mouse interaction.

Keyboard users should also receive visible focus feedback.

Example:

    .button:focus {
        transform: scale(1.03);
    }

A visible outline should generally remain available unless it is replaced with an equally clear focus indicator.

---

## 38. Accessibility and Motion

Animations should not make content difficult to use.

Some users prefer reduced motion.

CSS provides:

    @media (prefers-reduced-motion: reduce) {
        * {
            animation-duration: 0.01ms;
            animation-iteration-count: 1;
            transition-duration: 0.01ms;
        }
    }

The exact implementation can vary. The important principle is to respect the user's reduced-motion preference.

---

## 39. Avoid Excessive Animation

Too much animation can:

- Distract users
- Reduce readability
- Make interfaces feel slow
- Cause discomfort

Use animation to communicate or improve interaction rather than simply adding movement everywhere.

---

## 40. Common Mistakes

### Mistake 1

Putting the transition only inside `:hover`.

Better:

    .card {
        transition: transform 0.3s ease;
    }

### Mistake 2

Forgetting `@keyframes` when using a custom animation name.

### Mistake 3

Using extremely long animation durations for small interactions.

### Mistake 4

Animating too many properties unnecessarily.

### Mistake 5

Ignoring keyboard focus.

### Mistake 6

Ignoring reduced-motion preferences.

---

## 41. Practical Button Effect

    .button {
        transition:
            transform 0.2s ease,
            opacity 0.2s ease;
    }

    .button:hover {
        transform: translateY(-2px);
        opacity: 0.9;
    }

---

## 42. Practical Loading Animation

Example:

    @keyframes pulse {
        0% {
            opacity: 0.5;
        }

        50% {
            opacity: 1;
        }

        100% {
            opacity: 0.5;
        }
    }

    .loader {
        animation: pulse 1.5s ease-in-out infinite;
    }

---

## 📌 Key Takeaway

Remember:

    Transition → Smooth change between states

    Animation → Multi-step sequence using @keyframes

Important transition properties:

    transition-property
    transition-duration
    transition-timing-function
    transition-delay

Important animation properties:

    animation-name
    animation-duration
    animation-timing-function
    animation-delay
    animation-iteration-count
    animation-direction
    animation-fill-mode
    animation-play-state

**Transform + Transition = Smooth UI Effects**

**@keyframes + Animation = CSS Motion**