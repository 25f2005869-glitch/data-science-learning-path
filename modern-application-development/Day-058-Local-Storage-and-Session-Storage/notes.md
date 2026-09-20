# 📚 Day 058 — Local Storage and Session Storage

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 058  
**Topic:** Local Storage and Session Storage

---

## 1. What Is Web Storage?

Web Storage is a browser API that allows web applications to store data locally in the user's browser.

The two main storage objects are:

- `localStorage`
- `sessionStorage`

Both use a key-value model.

Example:

    localStorage.setItem("name", "Saloni");

Here:

- `name` is the key.
- `Saloni` is the value.

---

## 2. localStorage

`localStorage` stores data associated with the website's origin.

The data normally remains available after:

- Page refresh
- Closing the page
- Closing and reopening the browser

Example:

    localStorage.setItem("name", "Saloni");

Reading the value:

    const name = localStorage.getItem("name");

---

## 3. sessionStorage

`sessionStorage` also stores key-value data, but its lifetime is associated with the current page session and browsing context.

Example:

    sessionStorage.setItem("course", "MAD 1");

Reading:

    const course = sessionStorage.getItem("course");

A different tab generally has its own `sessionStorage`.

---

## 4. localStorage vs sessionStorage

| Feature | localStorage | sessionStorage |
|---|---|---|
| API | Web Storage API | Web Storage API |
| Key-value storage | Yes | Yes |
| Survives page refresh | Yes | Yes |
| Intended to persist after browser restart | Yes | No |
| Separate per origin | Yes | Yes |
| Separate browsing context | Yes | Yes |
| Main use | Persistent preferences/data | Temporary session data |

The exact lifetime of a browsing session can depend on the browser and its behavior.

---

## 5. setItem()

`setItem()` stores a value.

Syntax:

    storage.setItem(key, value);

Example:

    localStorage.setItem("theme", "dark");

Another example:

    sessionStorage.setItem("course", "MAD 1");

---

## 6. getItem()

`getItem()` retrieves a stored value.

Example:

    const theme = localStorage.getItem("theme");

If the key does not exist, `getItem()` returns:

    null

Example:

    const result = localStorage.getItem("unknown");

    console.log(result);

The result is `null`.

---

## 7. Updating Data

Calling `setItem()` with an existing key replaces its previous value.

Example:

    localStorage.setItem("theme", "light");

    localStorage.setItem("theme", "dark");

The final value is:

    dark

---

## 8. removeItem()

`removeItem()` deletes one stored key.

Example:

    localStorage.removeItem("theme");

The `theme` entry is removed.

---

## 9. clear()

`clear()` removes all entries from that storage object.

Example:

    localStorage.clear();

Be careful with `clear()` because it removes every entry stored by the current origin in that storage area.

---

## 10. key()

`key()` retrieves the key at a particular numeric index.

Example:

    const firstKey = localStorage.key(0);

Storage ordering should not be relied upon for application logic.

---

## 11. length

The `length` property tells you how many key-value entries exist.

Example:

    console.log(localStorage.length);

---

## 12. Storage Stores Strings

Web Storage stores values as strings.

Example:

    localStorage.setItem("age", 17);

When retrieved:

    const age = localStorage.getItem("age");

The retrieved value is:

    "17"

It is a string, not a JavaScript number.

---

## 13. Converting Strings Back to Numbers

If a number was stored as a string, convert it when necessary.

Example:

    localStorage.setItem("age", "17");

    const age =
        Number(localStorage.getItem("age"));

Now `age` is a number.

---

## 14. Boolean Values

Booleans are also converted to strings.

Example:

    localStorage.setItem("loggedIn", true);

The stored representation is:

    "true"

Reading:

    const value =
        localStorage.getItem("loggedIn");

This is a string.

A simple conversion can be:

    const loggedIn = value === "true";

---

## 15. Storing Objects

Web Storage cannot directly store a JavaScript object as an object.

Example:

    const student = {
        name: "Saloni",
        course: "MAD 1",
        score: 90
    };

Use `JSON.stringify()` first.

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

---

## 16. JSON.stringify()

`JSON.stringify()` converts a JavaScript value into a JSON string.

Example:

    const student = {
        name: "Saloni",
        score: 90
    };

    const data = JSON.stringify(student);

The result is a string containing JSON representation.

---

## 17. JSON.parse()

`JSON.parse()` converts valid JSON text back into a JavaScript value.

Example:

    const data =
        localStorage.getItem("student");

    const student =
        JSON.parse(data);

Now `student` is a JavaScript object.

---

## 18. Storing Arrays

Arrays can also be stored using JSON.

Example:

    const courses = [
        "MAD 1",
        "DBMS",
        "PDSA",
        "MLF"
    ];

    localStorage.setItem(
        "courses",
        JSON.stringify(courses)
    );

Read the array:

    const storedCourses =
        JSON.parse(
            localStorage.getItem("courses")
        );

---

## 19. Handling Missing Data

If a key does not exist:

    localStorage.getItem("student")

returns:

    null

Always consider this possibility before parsing.

Example:

    const data =
        localStorage.getItem("student");

    if (data !== null) {
        const student = JSON.parse(data);
    }

---

## 20. Default Values

The logical OR operator can provide a default string:

    const theme =
        localStorage.getItem("theme") || "light";

Another common approach is nullish coalescing:

    const theme =
        localStorage.getItem("theme") ?? "light";

---

## 21. Updating an Object in Storage

Suppose an object is already stored.

First retrieve it:

    const student =
        JSON.parse(
            localStorage.getItem("student")
        );

Update it:

    student.score = 95;

Store it again:

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

Web Storage does not automatically track changes inside a retrieved object.

---

## 22. Storage Events

The `storage` event can notify a document when storage changes in another browsing context of the same origin.

Example:

    window.addEventListener(
        "storage",
        function (event) {
            console.log(event.key);
            console.log(event.newValue);
        }
    );

Important point:

A storage change made in one document does not normally fire the `storage` event in that same document.

It is mainly useful for communication across other same-origin documents, such as another tab.

---

## 23. Practical Uses of localStorage

`localStorage` can be useful for:

- Theme preference
- Language preference
- UI preferences
- Non-sensitive drafts
- Simple client-side settings
- Small amounts of application state

Example:

    localStorage.setItem("theme", "dark");

---

## 24. Practical Uses of sessionStorage

`sessionStorage` can be useful for:

- Temporary form state
- Data needed only during a page session
- Temporary UI state
- Short-lived workflow information

Example:

    sessionStorage.setItem(
        "currentStep",
        "2"
    );

---

## 25. Storage and Cookies

Web Storage and cookies are different mechanisms.

Web Storage:

- Convenient key-value browser storage
- JavaScript can access it
- Not automatically sent with every HTTP request

Cookies:

- Small pieces of data associated with websites
- Can be configured with security-related attributes
- May be sent with HTTP requests

Do not treat Web Storage as a replacement for every cookie use case.

---

## 26. Security Considerations

Do not store sensitive information in Web Storage merely because it is convenient.

Avoid storing things such as:

- Passwords
- Authentication secrets
- Highly sensitive personal information
- Long-lived security tokens without understanding the risks

JavaScript running in the page can access Web Storage.

If an application has an XSS vulnerability, stored data may be exposed.

---

## 27. Storage Is Not a Database

Web Storage is designed for relatively small amounts of client-side data.

It is not a replacement for:

- SQLite
- PostgreSQL
- MySQL
- Server databases

Use an actual database when an application needs structured, shared, persistent backend data.

---

## 28. Storage Quotas

Browsers impose limits on Web Storage.

The exact available amount can vary by browser and environment.

Applications should not assume unlimited storage.

For larger client-side data requirements, technologies such as IndexedDB may be more appropriate.

---

## 29. Origin-Based Storage

Storage is associated with the web origin.

An origin is based on:

- Scheme
- Host
- Port

Different origins generally have separate storage areas.

For example:

    https://example.com

and:

    https://another-example.com

do not normally share the same Web Storage.

---

## 30. Storage API Summary

Common methods and properties:

    setItem()
    getItem()
    removeItem()
    clear()
    key()
    length

---

## 31. Example: Theme Preference

Store:

    localStorage.setItem(
        "theme",
        "dark"
    );

Read:

    const theme =
        localStorage.getItem("theme");

Apply:

    document.body.dataset.theme = theme;

This allows a theme preference to survive page reloads.

---

## 32. Example: Student Progress

Create:

    const progress = {
        html: 100,
        css: 100,
        javascript: 60
    };

Store:

    localStorage.setItem(
        "progress",
        JSON.stringify(progress)
    );

Read:

    const storedProgress =
        JSON.parse(
            localStorage.getItem("progress")
        );

---

## 33. Common Mistakes

### Mistake 1: Expecting objects to remain objects

Incorrect assumption:

    localStorage.setItem("student", student);

Use:

    JSON.stringify(student)

### Mistake 2: Forgetting JSON.parse()

If an object was stored as JSON, parse it when retrieving.

### Mistake 3: Assuming numbers remain numbers

Web Storage returns strings.

### Mistake 4: Calling clear() unnecessarily

`clear()` removes all entries for that storage area.

### Mistake 5: Storing sensitive information

Web Storage is accessible to JavaScript running in the page.

### Mistake 6: Assuming storage is unlimited

Storage quotas exist.

---

## 34. Best Practices

- Use meaningful keys.
- Store only necessary data.
- Use JSON for arrays and objects.
- Handle missing values.
- Handle JSON parsing errors when data may be corrupted.
- Avoid sensitive data.
- Do not use Web Storage as a backend database.
- Keep stored data small.
- Use `sessionStorage` for temporary session-specific state.
- Use `localStorage` for suitable persistent preferences.

---

## 🧠 Key Takeaway

Web Storage provides simple browser-side key-value storage.

Remember:

    localStorage
    ↓
    Persistent browser-side storage

    sessionStorage
    ↓
    Temporary page-session storage

For objects and arrays:

    JavaScript Object
        ↓
    JSON.stringify()
        ↓
    String
        ↓
    Storage

And when reading:

    Storage
        ↓
    String
        ↓
    JSON.parse()
        ↓
    JavaScript Object