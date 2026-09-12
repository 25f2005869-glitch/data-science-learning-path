# ⚡ Day 014 — HTML Form Validation and Attributes Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🔹 Basic Validation

| Attribute | Purpose |
|---|---|
| `required` | Makes a field compulsory |
| `minlength` | Minimum number of characters |
| `maxlength` | Maximum number of characters |
| `min` | Minimum allowed value |
| `max` | Maximum allowed value |
| `pattern` | Requires a matching pattern |

---

## 🔹 Common Input Types

| Type | Purpose |
|---|---|
| `text` | General text |
| `email` | Email address |
| `password` | Password |
| `number` | Numeric value |
| `date` | Date |
| `url` | Website URL |
| `tel` | Telephone number |
| `search` | Search input |
| `file` | File selection |

---

## 🔹 Common Form Attributes

| Attribute | Purpose |
|---|---|
| `action` | Destination for submitted data |
| `method` | HTTP method |
| `autocomplete` | Browser autocomplete behavior |
| `novalidate` | Disables native browser validation |

---

## 🔹 Input Attributes

| Attribute | Purpose |
|---|---|
| `id` | Identifies an element |
| `name` | Name used when submitting data |
| `value` | Initial/current value |
| `placeholder` | Input hint |
| `required` | Required field |
| `disabled` | Disables control |
| `readonly` | Prevents editing |
| `checked` | Pre-selects checkbox/radio |
| `multiple` | Allows multiple selections where supported |

---

## 🔹 Validation Examples

    <input type="text" required>

    <input type="text" minlength="3">

    <input type="text" maxlength="20">

    <input type="number" min="18" max="100">

    <input type="email" required>

    <input type="url">

    <input type="text" pattern="[A-Za-z]+">

---

## 🔹 Password Example

    <input
        type="password"
        minlength="8"
        maxlength="20"
        required>

---

## 🔹 Radio Example

    <input type="radio" name="gender" value="male">
    <input type="radio" name="gender" value="female">

Radio buttons in the same group should normally use the same `name`.

---

## 🔹 Checkbox Example

    <input type="checkbox" name="skills" value="html">
    <input type="checkbox" name="skills" value="css">

Multiple checkboxes can be selected.

---

## 🔹 Dropdown Example

    <select name="course" required>
        <option value="">Select Course</option>
        <option value="mad">MAD</option>
        <option value="mlt">MLT</option>
    </select>

---

## 🔹 Disabled vs Readonly

`disabled`

- Cannot normally be edited
- Value is not submitted

`readonly`

- Cannot be edited
- Value can be submitted

---

## 🔹 Client vs Server Validation

Client-side:

    Browser → Validation → User Feedback

Server-side:

    Browser → Server → Validation → Processing

Always validate important data on the server.

---

## 🔹 Remember

`required` → Must enter

`minlength` → Minimum characters

`maxlength` → Maximum characters

`min` → Minimum value

`max` → Maximum value

`pattern` → Specific format

`placeholder` → Hint

`disabled` → Unavailable

`readonly` → Cannot edit

`checked` → Pre-selected

`selected` → Pre-selected option

`multiple` → Multiple selection

---

## ⭐ Quick Revision

HTML5 can perform many basic validation checks without JavaScript.

The most important validation attributes are:

`required` + `minlength` + `maxlength` + `min` + `max` + `pattern`

But client-side validation is not a replacement for server-side validation.