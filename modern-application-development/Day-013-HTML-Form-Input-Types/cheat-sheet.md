# ⚡ Day 013 — HTML Form Input Types Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)

---

# 🧱 Basic Syntax

    <input type="text">

The `type` attribute determines the input control.

---

# ⌨️ Text Inputs

    text
    → General text

    email
    → Email address

    password
    → Password

    search
    → Search query

    tel
    → Telephone number

    url
    → Website URL

---

# 🔢 Numeric Inputs

    number
    → Numeric value

    range
    → Slider/range value

Example:

    <input
        type="number"
        min="1"
        max="100">

---

# 📅 Date and Time

    date
    → Date

    time
    → Time

    datetime-local
    → Local date and time

    month
    → Month and year

    week
    → Week and year

---

# 🔘 Choice Inputs

## Radio

    <input
        type="radio"
        name="gender"
        value="male">

Use radio buttons when the user normally selects one option from a group.

---

## Checkbox

    <input
        type="checkbox"
        name="skills"
        value="html">

Use checkboxes when zero or more options can be selected.

---

# 📁 File

    <input
        type="file"
        name="resume">

Used for selecting files.

---

# 🎨 Color

    <input
        type="color"
        name="color">

Used for color selection.

---

# 👻 Hidden

    <input
        type="hidden"
        name="version"
        value="1">

Not visible to the user.

Hidden fields are not a security mechanism.

---

# 📤 Form Action Inputs

## Submit

    <input
        type="submit"
        value="Submit">

## Reset

    <input
        type="reset"
        value="Reset">

## Generic Button

    <input
        type="button"
        value="Click">

---

# 📊 Quick Reference

| Type | Purpose |
|---|---|
| `text` | General text |
| `email` | Email |
| `password` | Password |
| `number` | Number |
| `date` | Date |
| `time` | Time |
| `datetime-local` | Local date and time |
| `month` | Month and year |
| `week` | Week and year |
| `url` | Website URL |
| `tel` | Phone |
| `search` | Search |
| `radio` | One choice |
| `checkbox` | Multiple choices |
| `file` | File selection |
| `color` | Color |
| `range` | Range/slider |
| `hidden` | Hidden value |
| `submit` | Submit |
| `reset` | Reset |
| `button` | Generic button |

---

# 🏷️ Common Attributes

    id
    name
    value
    placeholder
    required
    disabled
    readonly

---

# 🔢 Number/Range Attributes

    min
    max
    step

Example:

    <input
        type="range"
        min="0"
        max="100"
        step="10">

---

# 🎯 Choosing the Correct Type

    Name
    → text

    Email
    → email

    Password
    → password

    Age
    → number

    Date of Birth
    → date

    Website
    → url

    Phone
    → tel

    Search
    → search

    Gender
    → radio

    Skills
    → checkbox

    Resume
    → file

---

# 🧠 Radio vs Checkbox

    Radio
    → Usually one option

    Checkbox
    → Zero or more options

---

# ⚠️ Important

Do not normally use:

    type="number"

for phone numbers.

Prefer:

    type="tel"

because phone numbers are identifiers rather than mathematical quantities.

---

# ♿ Accessibility

Use labels:

    <label for="email">
        Email:
    </label>

    <input
        type="email"
        id="email"
        name="email">

---

# ⭐ Memory Trick

    text      → Text
    email     → Email
    password  → Password
    number    → Number
    date      → Date
    tel       → Telephone
    url       → URL
    radio     → One
    checkbox  → Many
    file      → File
    submit    → Send
    reset     → Clear