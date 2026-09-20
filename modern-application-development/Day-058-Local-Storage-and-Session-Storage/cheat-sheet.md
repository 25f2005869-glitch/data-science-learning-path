# ⚡ Day 058 — Local Storage and Session Storage Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 058  
**Topic:** Local Storage and Session Storage

---

## 🔹 localStorage

Persistent browser-side key-value storage.

    localStorage.setItem("name", "Saloni");

---

## 🔹 sessionStorage

Storage associated with the current page session/browsing context.

    sessionStorage.setItem("course", "MAD 1");

---

## 🔹 Store Data

    localStorage.setItem(
        "key",
        "value"
    );

---

## 🔹 Read Data

    const value =
        localStorage.getItem("key");

If the key does not exist:

    null

---

## 🔹 Update Data

    localStorage.setItem(
        "theme",
        "light"
    );

    localStorage.setItem(
        "theme",
        "dark"
    );

The second value replaces the first.

---

## 🔹 Remove One Item

    localStorage.removeItem("theme");

---

## 🔹 Remove Everything

    localStorage.clear();

Be careful: this clears all entries in that storage area for the current origin.

---

## 🔹 Number

Storage values are strings.

    localStorage.setItem("age", "17");

    const age =
        Number(localStorage.getItem("age"));

---

## 🔹 Boolean

    localStorage.setItem(
        "loggedIn",
        "true"
    );

    const loggedIn =
        localStorage.getItem("loggedIn")
        === "true";

---

## 🔹 Object

Store:

    const student = {
        name: "Saloni",
        score: 90
    };

    localStorage.setItem(
        "student",
        JSON.stringify(student)
    );

Read:

    const student =
        JSON.parse(
            localStorage.getItem("student")
        );

---

## 🔹 Array

    const courses = [
        "MAD 1",
        "DBMS",
        "PDSA"
    ];

    localStorage.setItem(
        "courses",
        JSON.stringify(courses)
    );

Read:

    const courses =
        JSON.parse(
            localStorage.getItem("courses")
        );

---

## 🔹 Storage Properties

    localStorage.length

    localStorage.key(0)

---

## 🔹 Storage Event

    window.addEventListener(
        "storage",
        function (event) {
            console.log(event.key);
            console.log(event.newValue);
        }
    );

The event is mainly useful for changes made in another same-origin browsing context.

---

## 🔹 localStorage vs sessionStorage

| localStorage | sessionStorage |
|---|---|
| Persistent | Temporary |
| Survives reload | Survives reload |
| Suitable for preferences | Suitable for session state |
| Shared across same-origin documents according to storage rules | Associated with current browsing context |

---

## 🔹 Important Methods

    setItem()
    getItem()
    removeItem()
    clear()
    key()

Property:

    length

---

## 🔹 Important JSON Methods

    JSON.stringify()
    JSON.parse()

Remember:

    Object
      ↓
    stringify
      ↓
    String
      ↓
    Storage

    Storage
      ↓
    String
      ↓
    parse
      ↓
    Object

---

## ⚠️ Security

Do not store sensitive information such as passwords or security secrets in Web Storage.

---

## 🧠 Remember

    localStorage
    = persistent client-side storage

    sessionStorage
    = temporary session storage

    Web Storage
    = key + string value