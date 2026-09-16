# 🧪 Day 022 — CSS Selectors Practice

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 🎯 Practice Objective

The objective of Day 022 practice is to develop a strong understanding of CSS selectors and learn how to target HTML elements accurately.

---

# 🧠 Part 1 — Theory Questions

## Question 1

What is a CSS selector?

---

## Question 2

What does the universal selector select?

---

## Question 3

What is the difference between a class selector and an ID selector?

---

## Question 4

Why are classes useful for reusable styling?

---

## Question 5

What is a grouping selector?

---

## Question 6

What is the difference between a descendant selector and a child selector?

---

## Question 7

What does the `+` combinator mean?

---

## Question 8

What does the `~` combinator mean?

---

## Question 9

What is an attribute selector?

---

## Question 10

What is a pseudo-class?

---

## Question 11

What does `:hover` do?

---

## Question 12

What does `:nth-child()` do?

---

## Question 13

What is CSS specificity?

---

## Question 14

Which generally has greater specificity: an ID selector or a class selector?

---

## Question 15

Why should `!important` be avoided when it is not necessary?

---

# 📝 Part 2 — Multiple Choice Questions

## Question 1

Which selector selects all elements?

A. `all`  
B. `#`  
C. `*`  
D. `.`

---

## Question 2

Which symbol represents a class selector?

A. `#`  
B. `.`  
C. `*`  
D. `@`

---

## Question 3

Which symbol represents an ID selector?

A. `.`  
B. `#`  
C. `*`  
D. `&`

---

## Question 4

What does this selector select?

    div p

A. Only direct child paragraphs  
B. All paragraphs inside div  
C. All div elements  
D. Only the first paragraph

---

## Question 5

What does this selector mean?

    div > p

A. Any paragraph inside div  
B. Direct child paragraphs of div  
C. All div elements after p  
D. Every paragraph on the page

---

## Question 6

What does `:hover` represent?

A. An element that is hidden  
B. An element that is selected  
C. An element currently under the pointer  
D. An element that is disabled

---

## Question 7

Which selector targets email inputs?

A. `input.email`  
B. `input[email]`  
C. `input[type="email"]`  
D. `email.input`

---

## Question 8

Which selector targets the second list item?

A. `li:second`  
B. `li:nth-child(2)`  
C. `li:nth(2)`  
D. `li[2]`

---

## Question 9

Which has higher specificity?

A. Element selector  
B. Class selector  
C. ID selector  
D. Universal selector

---

## Question 10

Which selector selects elements having the `required` attribute?

A. `.required`  
B. `#required`  
C. `[required]`  
D. `required`

---

# 💻 Part 3 — Coding Exercises

## Exercise 1 — Element Selector

Create:

- One heading
- Three paragraphs

Use an element selector to change all paragraph text colors.

---

## Exercise 2 — Class Selector

Create three paragraphs.

Give two paragraphs the same class.

Style only those two paragraphs.

---

## Exercise 3 — ID Selector

Create one heading with an ID.

Use an ID selector to change its color.

---

## Exercise 4 — Grouping Selector

Style all of these using one CSS rule:

- `h1`
- `h2`
- `h3`

---

## Exercise 5 — Descendant Selector

Create a section containing:

- A paragraph
- A div
- Another paragraph inside the div

Use:

    section p

Observe which paragraphs are selected.

---

## Exercise 6 — Child Selector

Use:

    section > p

Compare its result with:

    section p

---

## Exercise 7 — Sibling Selectors

Create:

    h2
    p
    p

Test:

    h2 + p

Then test:

    h2 ~ p

Observe the difference.

---

## Exercise 8 — Attribute Selector

Create:

- Text input
- Email input
- Password input
- Number input

Use attribute selectors to style each type differently.

---

## Exercise 9 — Pseudo-Class

Create a button.

Use:

    button:hover

Change its appearance when the pointer moves over it.

---

## Exercise 10 — Focus

Create an input field.

Use:

    input:focus

Change its background when the input receives focus.

---

# 🚀 Part 4 — Mini Challenge

Create a **CSS Selector Demonstration Page**.

The page should contain:

### Section 1

Heading and paragraphs.

Use an element selector.

### Section 2

Three cards.

Use a class selector.

### Section 3

One special card.

Use an ID selector.

### Section 4

Nested content.

Demonstrate descendant and child selectors.

### Section 5

List.

Demonstrate:

- `:first-child`
- `:last-child`
- `:nth-child()`

### Section 6

Form.

Demonstrate:

- Attribute selectors
- `:focus`
- `:checked`
- `:disabled`

### Section 7

Links.

Demonstrate:

- `:hover`

---

# 🐞 Part 5 — Debugging

Find the problems in the following CSS:

    .student {
        color: blue;
    }

    student {
        color: red;
    }

    #student {
        color: green;
    }

Determine which selector requires:

- `.`
- `#`
- Element selector syntax

---

# 🧠 Part 6 — Specificity Practice

Consider:

    p {
        color: blue;
    }

    .text {
        color: green;
    }

    #special {
        color: red;
    }

HTML:

    <p id="special" class="text">
        Hello CSS
    </p>

Question:

Which color should normally be applied?

Explain why.

---

# 🔍 Part 7 — Selector Identification

Identify the selector type:

| Selector | Type |
|---|---|
| `*` | ? |
| `p` | ? |
| `.box` | ? |
| `#title` | ? |
| `div p` | ? |
| `div > p` | ? |
| `h2 + p` | ? |
| `h2 ~ p` | ? |
| `[required]` | ? |
| `a:hover` | ? |

---

# 📊 Part 8 — Self Assessment

Rate your understanding from 1 to 5.

| Skill | Score |
|---|---:|
| Universal selector | /5 |
| Element selector | /5 |
| Class selector | /5 |
| ID selector | /5 |
| Grouping selector | /5 |
| Descendant selector | /5 |
| Child selector | /5 |
| Sibling selectors | /5 |
| Attribute selectors | /5 |
| Pseudo-classes | /5 |
| Specificity | /5 |

---

# 🏁 Completion Checklist

- [ ] Universal selector practiced
- [ ] Element selector practiced
- [ ] Class selector practiced
- [ ] ID selector practiced
- [ ] Grouping selector practiced
- [ ] Descendant selector practiced
- [ ] Child selector practiced
- [ ] Sibling selectors practiced
- [ ] Attribute selectors practiced
- [ ] Pseudo-classes practiced
- [ ] Specificity understood
- [ ] Mini challenge completed
- [ ] Self-assessment completed

---

# 🎓 Expected Outcome

After completing Day 022, you should be able to identify and select HTML elements using different CSS selector techniques.

The next step is to learn how CSS handles:

**Colors, Backgrounds and Visual Appearance.**

---

**End of Day 022 Practice**