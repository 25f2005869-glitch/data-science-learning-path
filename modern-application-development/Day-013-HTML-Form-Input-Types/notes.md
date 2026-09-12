
### `notes.md`

```markdown
# 📝 Day 013 — HTML Form Input Types Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)

---

# 1. Introduction

HTML provides the `<input>` element for creating many different types of form controls.

The input type is determined by the `type` attribute.

For example:

    <input type="text">

    <input type="email">

    <input type="password">

    <input type="number">

Different input types are designed for different kinds of data.

---

# 2. The `<input>` Element

The `<input>` element is used to accept user input.

Basic syntax:

    <input type="text">

The `type` attribute determines how the input behaves.

Examples:

    text
    email
    password
    number
    date
    radio
    checkbox
    file

---

# 3. Text Input

The `text` type is used for general single-line text.

Example:

    <input
        type="text"
        name="full_name">

Common uses:

- Name
- Username
- City
- Subject
- Short description

---

# 4. Email Input

The `email` type is designed for email addresses.

Example:

    <input
        type="email"
        name="email">

Browsers can provide basic validation for email input.

Example:

    student@example.com

An email input does not automatically send email or verify that an address exists.

---

# 5. Password Input

The `password` type is used for password entry.

Example:

    <input
        type="password"
        name="password">

Characters are visually hidden by the browser.

Important:

Using `type="password"` alone does not provide complete security.

Real applications also require secure server-side handling and HTTPS.

---

# 6. Number Input

The `number` type is designed for numeric values.

Example:

    <input
        type="number"
        name="age">

Useful attributes include:

    min
    max
    step

Example:

    <input
        type="number"
        name="age"
        min="1"
        max="100">

---

# 7. Date Input

The `date` type allows users to select a date.

Example:

    <input
        type="date"
        name="dob">

The browser may display a date picker.

The exact appearance depends on the browser and operating system.

---

# 8. Time Input

The `time` type allows users to enter or select a time.

Example:

    <input
        type="time"
        name="appointment_time">

The browser may provide a time picker.

---

# 9. Datetime-Local Input

The `datetime-local` type allows the user to select a local date and time.

Example:

    <input
        type="datetime-local"
        name="meeting">

It represents a date and time without a timezone.

---

# 10. Month Input

The `month` type allows the user to select a month and year.

Example:

    <input
        type="month"
        name="semester">

A possible value can represent:

    2026-09

---

# 11. Week Input

The `week` type allows the user to select a week and year.

Example:

    <input
        type="week"
        name="study_week">

It can be useful for applications that organize information by calendar week.

---

# 12. URL Input

The `url` type is intended for website addresses.

Example:

    <input
        type="url"
        name="website">

Example value:

    https://example.com

Browsers can provide basic validation for URL input.

---

# 13. Telephone Input

The `tel` type is used for telephone numbers.

Example:

    <input
        type="tel"
        name="phone">

Unlike `number`, telephone numbers are generally treated as strings.

This is important because phone numbers can contain:

- Leading zeros
- Country codes
- Spaces
- Hyphens
- Parentheses

Example:

    +91 98765 43210

---

# 14. Search Input

The `search` type is designed for search queries.

Example:

    <input
        type="search"
        name="query"
        placeholder="Search...">

It is semantically appropriate for search fields.

---

# 15. Radio Buttons

The `radio` type allows the user to select one option from a group.

Example:

    <input
        type="radio"
        id="male"
        name="gender"
        value="male">

    <label for="male">
        Male
    </label>

For radio buttons to behave as one group, they should normally have the same `name`.

Example:

    name="gender"

---

# 16. Radio Button Group

Example:

    <input
        type="radio"
        id="beginner"
        name="level"
        value="beginner">

    <label for="beginner">
        Beginner
    </label>

    <input
        type="radio"
        id="advanced"
        name="level"
        value="advanced">

    <label for="advanced">
        Advanced
    </label>

Because both controls have:

    name="level"

the user can normally select only one of them.

---

# 17. Checkbox

The `checkbox` type allows users to select zero or more options.

Example:

    <input
        type="checkbox"
        id="html"
        name="skills"
        value="html">

    <label for="html">
        HTML
    </label>

Multiple checkboxes can be selected.

---

# 18. Checkbox Example

Example:

    HTML
    CSS
    JavaScript

A user can select:

    HTML + CSS

or:

    HTML + CSS + JavaScript

depending on the requirements.

Checkboxes are suitable when multiple choices are allowed.

---

# 19. Radio vs Checkbox

The main difference is:

    Radio
    ↓
    Usually one option from a group

    Checkbox
    ↓
    Zero or more options

Example:

Gender:

    ○ Male
    ○ Female
    ○ Other

This can use radio buttons.

Skills:

    ☑ HTML
    ☑ CSS
    ☐ JavaScript

This can use checkboxes.

---

# 20. File Input

The `file` type allows the user to select a file.

Example:

    <input
        type="file"
        name="resume">

The browser opens a file-selection interface.

For uploading files to a server, the form must also be configured appropriately, including the correct form encoding.

---

# 21. Color Input

The `color` type allows the user to select a color.

Example:

    <input
        type="color"
        name="favorite_color">

The browser may display a color picker.

---

# 22. Range Input

The `range` type creates a slider.

Example:

    <input
        type="range"
        name="volume"
        min="0"
        max="100">

The user can select a value within the specified range.

Useful attributes include:

    min
    max
    step

---

# 23. Hidden Input

The `hidden` type creates a form control that is not displayed to the user.

Example:

    <input
        type="hidden"
        name="form_version"
        value="1">

Hidden inputs can carry additional form data.

Important:

Hidden inputs are not a security mechanism.

A user can inspect and modify client-side form data.

Sensitive information should not be trusted simply because it is hidden.

---

# 24. Submit Input

The `submit` type creates a control that submits the form.

Example:

    <input
        type="submit"
        value="Submit">

A `<button type="submit">` can also be used.

---

# 25. Reset Input

The `reset` type creates a control that resets form controls to their initial values.

Example:

    <input
        type="reset"
        value="Reset">

A button can also be used:

    <button type="reset">
        Reset
    </button>

---

# 26. Button Input

The `button` type creates a generic button.

Example:

    <input
        type="button"
        value="Click Me">

Unlike a submit control, a generic button does not automatically submit the form.

It is commonly used with JavaScript to perform a custom action.

---

# 27. Input Type Comparison

    text
    → General text

    email
    → Email address

    password
    → Password

    number
    → Numeric value

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

    url
    → Website address

    tel
    → Telephone number

    search
    → Search query

    radio
    → One choice from a group

    checkbox
    → Zero or more choices

    file
    → File selection

    color
    → Color selection

    range
    → Value from a range

    hidden
    → Hidden form data

    submit
    → Submit form

    reset
    → Reset form

    button
    → Generic button

---

# 28. Choosing the Correct Input Type

Choosing the correct input type is important.

Examples:

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

    Phone Number
    → tel

    Search
    → search

    Gender
    → radio

    Skills
    → checkbox

---

# 29. Input Attributes Used with Different Types

Many input types can use common attributes such as:

    id
    name
    value
    placeholder
    required
    disabled
    readonly

Some types also commonly use:

    min
    max
    step

Example:

    <input
        type="number"
        name="age"
        min="1"
        max="100"
        step="1">

---

# 30. Input Type and Validation

Some input types provide built-in browser behavior and validation.

For example:

    <input type="email">

can help the browser recognize that the value should have an email-like format.

Similarly:

    <input type="url">

is intended for URL values.

However, client-side validation should not replace server-side validation.

The server must validate data independently.

---

# 31. Input Type and User Experience

Using the correct input type can improve the user experience.

For example:

    type="date"

may provide a date picker.

    type="number"

may provide numeric controls.

    type="email"

can provide an email-appropriate keyboard on some mobile devices.

    type="tel"

can provide a telephone-oriented keyboard on some mobile devices.

The exact UI depends on the browser and device.

---

# 32. Common Mistake — Using Number for Phone Numbers

A phone number should generally not be represented as:

    <input type="number">

Instead, use:

    <input type="tel">

Why?

Phone numbers are identifiers, not mathematical quantities.

They may contain:

    +91
    spaces
    hyphens
    leading zeros

---

# 33. Common Mistake — Radio Buttons with Different Names

If radio buttons are intended to be one group, they should normally share the same `name`.

Correct:

    <input
        type="radio"
        name="gender"
        value="male">

    <input
        type="radio"
        name="gender"
        value="female">

Incorrect grouping:

    <input
        type="radio"
        name="male"
        value="male">

    <input
        type="radio"
        name="female"
        value="female">

Using different names prevents the browser from treating them as the same radio group.

---

# 34. Common Mistake — Using Checkbox for Single Choice

If exactly one option should be selected, radio buttons are usually more appropriate.

Use:

    radio → One choice

Use:

    checkbox → Multiple choices

---

# 35. Input Types and Accessibility

Good forms should:

- Use meaningful labels.
- Use appropriate input types.
- Use unique `id` values.
- Associate labels using `for` and `id`.
- Provide clear instructions when necessary.
- Avoid relying only on placeholders.

Example:

    <label for="email">
        Email:
    </label>

    <input
        type="email"
        id="email"
        name="email">

---

# 36. Practical Form Example

A student registration form may use:

    Full Name
    → text

    Email
    → email

    Password
    → password

    Age
    → number

    Date of Birth
    → date

    Gender
    → radio

    Skills
    → checkbox

    Resume
    → file

    Website
    → url

    Phone
    → tel

This demonstrates why choosing the correct input type matters.

---

# 37. Day 013 Summary

In Day 013, I learned different HTML form input types.

Important types include:

- text
- email
- password
- number
- date
- time
- datetime-local
- month
- week
- url
- tel
- search
- radio
- checkbox
- file
- color
- range
- hidden
- submit
- reset
- button

I also learned how to choose an appropriate input type based on the data being collected.

---

# 🎯 Key Takeaways

    text      → General text
    email     → Email
    password  → Password
    number    → Number
    date      → Date
    time      → Time
    url       → Website URL
    tel       → Phone number
    search    → Search
    radio     → One choice
    checkbox  → Multiple choices
    file      → File selection
    color     → Color selection
    range     → Slider
    hidden    → Hidden form value
    submit    → Submit form
    reset     → Reset form
    button    → Generic button

---

# ⭐ Final Learning Goal

By the end of Day 013, I should be able to choose and use the correct HTML input type for different kinds of user data and explain why that input type is appropriate.

---

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development (MAD 1)