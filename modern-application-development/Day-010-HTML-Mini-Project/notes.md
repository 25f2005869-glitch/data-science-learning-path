
---

# 2️⃣ `notes.md`

```markdown
# 📝 Day 010 — HTML Mini Project Notes

## 1. Introduction

Day 010 is a practical mini project day.

The objective is to combine the HTML concepts learned in Days 001–009 into one complete webpage.

We will create a simple:

**Student Portfolio Website**

---

# 2. Project Structure

A basic HTML project contains:

```text
project/
└── code/
    └── index.html

    3. HTML Document Structure

Every HTML5 webpage normally starts with:

<!DOCTYPE html>

<html lang="en">

<head>
    ...
</head>

<body>
    ...
</body>

</html>
DOCTYPE
<!DOCTYPE html>

It tells the browser that the document uses HTML5.

4. Header

The <header> element contains introductory content.

Example:

<header>
    <h1>My Student Portfolio</h1>
    <p>Welcome to my portfolio.</p>
</header>
5. Navigation

The <nav> element contains important navigation links.

Example:

<nav>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
</nav>

Here:

#about

points to an element having:

id="about"
6. Main Content

The <main> element contains the primary content of the webpage.

Example:

<main>

    <section>
        <h2>About Me</h2>
        <p>...</p>
    </section>

</main>
7. Sections

A <section> represents a meaningful section of content.

Example:

<section id="skills">

    <h2>My Skills</h2>

    <ul>
        <li>Python</li>
        <li>HTML</li>
        <li>SQL</li>
    </ul>

</section>
8. Images

Images can be added using:

<img src="image.jpg" alt="Description">

Important attributes:

src → image location
alt → alternative text
width → image width
height → image height
9. Lists
Unordered List
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
Ordered List
<ol>
    <li>Learn HTML</li>
    <li>Learn CSS</li>
    <li>Learn JavaScript</li>
</ol>
10. Tables

A table can represent structured information.

Example:

<table border="1">

    <tr>
        <th>Course</th>
        <th>Status</th>
    </tr>

    <tr>
        <td>HTML</td>
        <td>Completed</td>
    </tr>

</table>

Important elements:

<table>
<tr>
<th>
<td>
11. Forms

Forms collect information from users.

Example:

<form>

    <label for="name">Name:</label>

    <input
        type="text"
        id="name"
        name="name"
        required>

    <button type="submit">
        Submit
    </button>

</form>
12. Article

An <article> represents independent content.

Example:

<article>

    <h3>My First Project</h3>

    <p>
        This project helped me understand HTML.
    </p>

</article>
13. Aside

The <aside> element contains related or secondary content.

Example:

<aside>

    <h2>Currently Learning</h2>

    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>

</aside>
14. Footer

The <footer> usually contains copyright or additional information.

Example:

<footer>

    <p>
        © 2026 Student Portfolio
    </p>

</footer>
15. Complete Project Flow

The webpage structure can be visualized as:

HTML
│
├── HEAD
│   ├── charset
│   ├── viewport
│   └── title
│
└── BODY
    │
    ├── HEADER
    │
    ├── NAV
    │
    ├── MAIN
    │   ├── ABOUT
    │   ├── EDUCATION
    │   ├── SKILLS
    │   ├── PROJECTS
    │   └── CONTACT
    │
    ├── ASIDE
    │
    └── FOOTER
16. Important Learning

The most important goal of this project is not making the webpage beautiful.

The goal is understanding:

How different HTML elements work together to create a complete webpage.

CSS will later be used to improve the visual design.

17. Best Practices
Use semantic HTML.
Use meaningful headings.
Use alt text for images.
Use labels with form inputs.
Maintain proper indentation.
Use meaningful id values.
Keep content organized.
Use one main <h1> for the page.

---

# 3️⃣ `cheat-sheet.md`

```markdown
# ⚡ Day 010 — HTML Mini Project Cheat Sheet

## 📄 Basic Structure

```html
<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>My Website</title>
</head>

<body>

</body>

</html>
🧱 Semantic Elements
Element	Purpose
<header>	Introductory content
<nav>	Navigation links
<main>	Main webpage content
<section>	Content section
<article>	Independent content
<aside>	Related/secondary content
<footer>	Footer information
<figure>	Image/media content
<figcaption>	Figure description
🔗 Link
<a href="https://example.com" target="_blank">
    Visit Website
</a>
🖼 Image
<img
    src="image.jpg"
    alt="Image Description"
    width="200">
📋 Unordered List
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
🔢 Ordered List
<ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
📊 Table
<table border="1">

    <tr>
        <th>Name</th>
        <th>Course</th>
    </tr>

    <tr>
        <td>Student</td>
        <td>MAD</td>
    </tr>

</table>
📝 Form
<form>

    <label for="name">
        Name:
    </label>

    <input
        type="text"
        id="name"
        name="name"
        required>

    <button type="submit">
        Submit
    </button>

</form>
🔗 Internal Navigation
<a href="#about">
    About
</a>

<section id="about">

    <h2>About Me</h2>

</section>
🎯 Important Attributes
Attribute	Purpose
id	Unique element identifier
class	Groups elements
href	Link destination
src	Resource location
alt	Alternative image text
target	Link opening behavior
name	Form field name
value	Form field value
placeholder	Input hint
required	Makes input mandatory
🧠 Remember
HTML = Structure
CSS = Styling
JavaScript = Behaviour
