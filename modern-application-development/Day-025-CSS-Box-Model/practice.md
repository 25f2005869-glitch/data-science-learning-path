# 🧪 Day 025 — CSS Box Model Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🎯 Practice Objective

This practice file is designed to strengthen the understanding of the CSS Box Model through:

- Theory questions
- Multiple-choice questions
- Box Model calculations
- CSS coding exercises
- Debugging
- Mini project
- Self-assessment

---

# 📘 Part 1 — Theory Questions

## Q1. What is the CSS Box Model?

Write your answer.

---

## Q2. What are the four main components of the CSS Box Model?

Write your answer.

---

## Q3. What is the Content area?

Write your answer.

---

## Q4. What is Padding?

Write your answer.

---

## Q5. What is Border?

Write your answer.

---

## Q6. What is Margin?

Write your answer.

---

## Q7. What is the difference between Padding and Margin?

Write your answer.

---

## Q8. What does the `box-sizing` property do?

Write your answer.

---

## Q9. What is the difference between `content-box` and `border-box`?

Write your answer.

---

## Q10. What does `margin: 0 auto` commonly do?

Write your answer.

---

## Q11. What is margin collapsing?

Write your answer.

---

# 📝 Part 2 — Multiple Choice Questions

## Q12. Which part is closest to the actual content?

A. Margin  
B. Border  
C. Padding  
D. Content

**Answer:** __________

---

## Q13. Which property creates space between content and border?

A. `margin`  
B. `padding`  
C. `border`  
D. `spacing`

**Answer:** __________

---

## Q14. Which property creates space outside the border?

A. `padding`  
B. `margin`  
C. `content`  
D. `border`

**Answer:** __________

---

## Q15. What is the default value of `box-sizing`?

A. `border-box`  
B. `padding-box`  
C. `content-box`  
D. `margin-box`

**Answer:** __________

---

## Q16. Which value makes the declared width include padding and border?

A. `content-box`  
B. `border-box`  
C. `padding-box`  
D. `margin-box`

**Answer:** __________

---

## Q17. Which declaration creates a 2px solid black border?

A. `border: black 2px;`  
B. `border: 2px solid black;`  
C. `border: solid black;`  
D. `border: 2 black solid;`

**Answer:** __________

---

## Q18. Which property creates rounded corners?

A. `corner-radius`  
B. `radius`  
C. `border-radius`  
D. `box-radius`

**Answer:** __________

---

## Q19. Which declaration is commonly used to center a fixed-width block?

A. `padding: auto;`  
B. `margin: auto 0;`  
C. `margin: 0 auto;`  
D. `align: center;`

**Answer:** __________

---

## Q20. Which shorthand order is correct for four values?

A. Right → Left → Top → Bottom  
B. Top → Right → Bottom → Left  
C. Top → Bottom → Left → Right  
D. Left → Right → Top → Bottom

**Answer:** __________

---

# 🧮 Part 3 — Box Model Calculations

## Q21. Calculate Total Width

Given:

    width: 300px;
    padding: 20px;
    border: 5px solid black;

Assume:

    box-sizing: content-box;

Calculate the total outer width.

**Answer:** __________

---

## Q22. Calculate Total Width

Given:

    width: 300px;
    padding: 20px;
    border: 5px solid black;
    box-sizing: border-box;

Calculate the total outer width.

**Answer:** __________

---

## Q23. Calculate Total Width

Given:

    Content width = 200px
    Left padding = 10px
    Right padding = 10px
    Left border = 2px
    Right border = 2px

Calculate the total width.

**Answer:** __________

---

## Q24. Calculate Total Height

Given:

    Content height = 150px
    Top padding = 10px
    Bottom padding = 10px
    Top border = 2px
    Bottom border = 2px

Calculate the total height.

**Answer:** __________

---

## Q25. Calculate Total Width

Given:

    Content width = 400px
    Left padding = 30px
    Right padding = 30px
    Left border = 3px
    Right border = 3px

Calculate the total width.

**Answer:** __________

---

# 💻 Part 4 — Coding Practice

## Exercise 1 — Basic Box

Create a box with:

    width: 300px;
    height: 150px;
    padding: 20px;
    border: 2px solid black;
    margin: 20px;

Add some text inside the box.

---

## Exercise 2 — Padding Shorthand

Create a box with:

    Top = 10px
    Right = 20px
    Bottom = 30px
    Left = 40px

Use only the padding shorthand property.

---

## Exercise 3 — Margin Shorthand

Create a box with:

    Top = 10px
    Right = 20px
    Bottom = 30px
    Left = 40px

Use only the margin shorthand property.

---

## Exercise 4 — Border Styles

Create four boxes demonstrating:

- Solid border
- Dashed border
- Dotted border
- Double border

---

## Exercise 5 — Rounded Card

Create a student card with:

    width: 300px;
    padding: 20px;
    border: 2px solid black;
    border-radius: 15px;
    margin: 20px auto;

The card should contain:

- Student name
- Programme
- Skills
- Learning goal

---

## Exercise 6 — Content Box

Create an element using:

    width: 300px;
    padding: 20px;
    border: 5px solid black;
    box-sizing: content-box;

Calculate and verify its actual width.

---

## Exercise 7 — Border Box

Create another element using:

    width: 300px;
    padding: 20px;
    border: 5px solid black;
    box-sizing: border-box;

Compare it with the previous element.

---

## Exercise 8 — Center a Container

Create a container with:

    width: 500px;
    margin: 0 auto;

Add content inside it.

Make sure the container is centered horizontally.

---

# 🐞 Part 5 — Debugging Practice

## Q26. Find and Fix the Errors

Given:

    .box {
        width: 300;
        height: 200;
        padding: 20;
        border: black 2;
        margin auto;
    }

Identify and correct all invalid declarations.

---

## Q27. Find the Box Model Mistake

Given:

    .card {
        width: 300px;
        padding: 30px;
        border: 5px solid black;
    }

The developer expects the total width to remain 300px.

What should be added?

Write the corrected CSS declaration.

---

## Q28. Padding or Margin?

A developer wants to create space between the text and the border.

Should they use:

- Padding
- Margin

**Answer:** __________

---

## Q29. Padding or Margin?

A developer wants to create space between two cards.

Should they use:

- Padding
- Margin

**Answer:** __________

---

# 🏗️ Part 6 — Mini Challenge

## Student Profile Card

Create a complete Student Profile Card using HTML and CSS.

The card should contain:

- Student name
- Programme
- Short introduction
- Education
- Skills
- Learning goal

Apply the following CSS properties:

    width
    padding
    border
    border-radius
    margin
    box-sizing
    font-size
    font-weight
    text-align
    background-color

Requirements:

- The card should have a fixed maximum width.
- The card should be centered horizontally.
- Content should have proper internal spacing.
- The card should have a visible border.
- Corners should be rounded.
- Use `box-sizing: border-box`.

---

# 🔍 Part 7 — Property Identification

Identify the correct CSS property.

## Q30.

Controls the width of an element:

**Answer:** __________

---

## Q31.

Controls the height of an element:

**Answer:** __________

---

## Q32.

Creates internal spacing:

**Answer:** __________

---

## Q33.

Creates external spacing:

**Answer:** __________

---

## Q34.

Creates a boundary around the element:

**Answer:** __________

---

## Q35.

Creates rounded corners:

**Answer:** __________

---

## Q36.

Controls how width and height are calculated:

**Answer:** __________

---

## Q37.

Sets the minimum width:

**Answer:** __________

---

## Q38.

Sets the maximum width:

**Answer:** __________

---

# 🧠 Part 8 — Quick Concept Test

Complete the statements.

## Q39.

The four components of the CSS Box Model are:

    __________ → __________ → __________ → __________

---

## Q40.

Padding is the space __________ the border.

**Answer:** __________

---

## Q41.

Margin is the space __________ the border.

**Answer:** __________

---

## Q42.

The default value of `box-sizing` is:

**Answer:** __________

---

## Q43.

`border-box` includes:

    __________ + __________ + __________

---

## Q44.

The shorthand order for four margin or padding values is:

    __________ → __________ → __________ → __________

---

# 📊 Part 9 — Comparison Practice

Complete the table.

| Feature | Padding | Margin |
|---|---|---|
| Inside the border? | __________ | __________ |
| Outside the border? | __________ | __________ |
| Creates internal spacing? | __________ | __________ |
| Creates external spacing? | __________ | __________ |
| Background can extend into the area? | __________ | __________ |

---

# 🔬 Part 10 — Experiment

Create two boxes with exactly the same:

    width: 300px;
    padding: 20px;
    border: 5px solid black;

Box 1:

    box-sizing: content-box;

Box 2:

    box-sizing: border-box;

Observe:

- Outer width
- Content area
- Effect of padding
- Effect of border

Write your observations below.

### Observation

    Box 1:
    ______________________________________

    Box 2:
    ______________________________________

    Main Difference:
    ______________________________________

---

# 🎯 Part 11 — Real-World Practice

Identify which Box Model property you would use.

### Situation 1

Add space inside a button around its text.

**Property:** __________

---

### Situation 2

Create space between two buttons.

**Property:** __________

---

### Situation 3

Create a visible outline around a card.

**Property:** __________

---

### Situation 4

Make a card have rounded corners.

**Property:** __________

---

### Situation 5

Center a fixed-width container horizontally.

**Property/Technique:** __________

---

### Situation 6

Make declared width include padding and border.

**Property:** __________

---

# 📋 Part 12 — Self Assessment

Rate yourself from 1 to 5.

| Skill | Rating |
|---|---:|
| CSS Box Model | /5 |
| Content | /5 |
| Padding | /5 |
| Padding Shorthand | /5 |
| Border | /5 |
| Border Radius | /5 |
| Margin | /5 |
| Margin Shorthand | /5 |
| Width and Height | /5 |
| `content-box` | /5 |
| `border-box` | /5 |
| Box Model Calculations | /5 |
| Margin Collapsing | /5 |
| Centering with Auto Margin | /5 |

---

# ✅ Completion Checklist

- [ ] I understand the CSS Box Model.
- [ ] I understand Content.
- [ ] I understand Padding.
- [ ] I understand Border.
- [ ] I understand Margin.
- [ ] I can use padding shorthand.
- [ ] I can use margin shorthand.
- [ ] I understand `width` and `height`.
- [ ] I understand `min-width` and `max-width`.
- [ ] I understand `border-radius`.
- [ ] I understand `content-box`.
- [ ] I understand `border-box`.
- [ ] I can calculate total element dimensions.
- [ ] I understand the difference between padding and margin.
- [ ] I understand margin collapsing.
- [ ] I can center a fixed-width block.
- [ ] I completed all coding exercises.
- [ ] I completed the mini challenge.
- [ ] I completed the debugging exercises.
- [ ] I completed the self-assessment.

---

## ⭐ Day 025 Practice Goal

The main goal is to become comfortable with the relationship:

    Content
       ↓
    Padding
       ↓
    Border
       ↓
    Margin

Once the Box Model becomes clear, CSS spacing and layout become much easier to understand.