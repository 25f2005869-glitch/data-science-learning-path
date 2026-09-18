# ⚡ Day 037 — CSS Transitions and Animations Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 037  
**Topic:** CSS Transitions and Animations

---

## 🔄 Transition

Basic:

    transition: transform 0.3s ease;

Full form:

    transition:
        property
        duration
        timing-function
        delay;

---

## ⏱️ Transition Properties

    transition-property
    transition-duration
    transition-timing-function
    transition-delay

---

## 🎯 Timing Functions

    linear
    ease
    ease-in
    ease-out
    ease-in-out

---

## 🧩 Transform

Move:

    transform: translate(20px, 10px);

Horizontal:

    transform: translateX(20px);

Vertical:

    transform: translateY(-10px);

Scale:

    transform: scale(1.1);

Rotate:

    transform: rotate(5deg);

---

## 🖱️ Hover Effect

    .card {
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

---

## 🎬 Animation

Define:

    @keyframes slide {
        from {
            transform: translateX(0);
        }

        to {
            transform: translateX(100px);
        }
    }

Apply:

    animation: slide 2s ease-in-out;

---

## 📊 Keyframes

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

---

## 🔁 Animation Properties

    animation-name
    animation-duration
    animation-timing-function
    animation-delay
    animation-iteration-count
    animation-direction
    animation-fill-mode
    animation-play-state

---

## ♾️ Infinite Animation

    animation-iteration-count: infinite;

---

## 🔀 Direction

    normal
    reverse
    alternate
    alternate-reverse

---

## ⏸️ Play State

    animation-play-state: paused;

    animation-play-state: running;

---

## 📌 Transition vs Animation

    Transition → State change
    Animation  → Keyframe sequence

---

## ♿ Reduced Motion

    @media (prefers-reduced-motion: reduce) {
        * {
            animation-duration: 0.01ms;
            animation-iteration-count: 1;
            transition-duration: 0.01ms;
        }
    }

---

## ⭐ Remember

**Transition = Smooth State Change**

**Animation = Multi-Step Motion**

**Transform = Move / Scale / Rotate**