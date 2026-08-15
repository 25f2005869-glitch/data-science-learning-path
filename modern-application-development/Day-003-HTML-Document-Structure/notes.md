# 📘 Day 003 - HTML Document Structure

Welcome to **Day 003** of the Modern Application Development learning journey.

Today we will learn the complete structure of an HTML document.

---

# 📖 What is an HTML Document?

An HTML document is a text file that tells the browser how to display a webpage.

Every HTML page follows a standard structure.

Example:

```html
<!DOCTYPE html>
<html>
<head>

</head>

<body>

</body>
</html>
```

---

# 1️⃣ <!DOCTYPE html>

This is the first line of every HTML5 document.

Purpose

- Tells the browser that this is an HTML5 document.
- Helps the browser render the webpage correctly.

Example

```html
<!DOCTYPE html>
```

---

# 2️⃣ <html> Tag

This is the root element of an HTML page.

Everything written in HTML is placed inside this tag.

Example

```html
<html>

</html>
```

---

# 3️⃣ lang Attribute

The language of the webpage is defined here.

Example

```html
<html lang="en">
```

"en" means English.

---

# 4️⃣ <head> Tag

The head section stores information about the webpage.

The content inside `<head>` is not displayed on the webpage.

Example

```html
<head>

</head>
```

Common elements inside `<head>`

- title
- meta
- link
- style
- script

---

# 5️⃣ <meta> Tag

The meta tag provides information about the webpage.

Example

```html
<meta charset="UTF-8">
```

This supports many languages and special characters.

---

Another example

```html
<meta name="viewport"
content="width=device-width, initial-scale=1.0">
```

This makes webpages responsive on mobile devices.

---

# 6️⃣ <title> Tag

Defines the title displayed in the browser tab.

Example

```html
<title>Day 003</title>
```

---

# 7️⃣ <body> Tag

Everything visible on the webpage is written inside the body tag.

Examples

- Headings
- Paragraphs
- Images
- Lists
- Links
- Tables

Example

```html
<body>

<h1>Hello World</h1>

<p>Welcome</p>

</body>
```

---

# 8️⃣ HTML Comments

Comments are ignored by the browser.

They are used to explain code.

Example

```html
<!-- This is a comment -->
```

---

# Complete HTML Structure

```html
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>My First Webpage</title>

</head>

<body>

<h1>Hello World</h1>

<p>Welcome to HTML.</p>

</body>

</html>
```

---

# Summary

Today you learned

- HTML Document
- DOCTYPE
- html Tag
- head Tag
- meta Tag
- title Tag
- body Tag
- HTML Comments

Congratulations!