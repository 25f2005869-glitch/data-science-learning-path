# 📘 Day 002 - How the Web Works

Welcome to **Day 002** of the **Modern Application Development** learning journey.

In this lesson, we will understand how the Internet and the World Wide Web work together to display a webpage in your browser.

---

# 🌍 What is the Internet?

The **Internet** is a worldwide network of connected computers and devices that allows them to communicate and share information.

It is often called the **Network of Networks** because millions of networks are connected together.

### Examples

- Watching YouTube videos
- Browsing Google
- Sending Emails
- Using WhatsApp Web
- Shopping on Amazon

All these services use the Internet.

---

# 🌐 What is the World Wide Web (WWW)?

The **World Wide Web (WWW)** is a collection of websites and web pages that are accessed using the Internet.

The Internet provides the connection, while the Web provides the content.

**Example**

- Internet → Road
- Website → House on the road

---

# 💻 What is a Web Browser?

A **Web Browser** is software used to access websites on the Internet.

Popular browsers include:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari
- Opera

A browser sends requests to web servers and displays the returned webpages.

---

# 🖥 What is a Web Server?

A **Web Server** is a computer that stores websites and delivers them to users when requested.

Examples of web server software:

- Apache
- Nginx
- IIS

When you open a website, the server sends the required HTML, CSS, JavaScript, images, and other files to your browser.

---

# 👥 Client and Server

## Client

A **Client** is the device or application that requests information.

Examples:

- Chrome Browser
- Firefox Browser
- Mobile Browser

## Server

A **Server** is the computer that stores and provides website data.

Example:

When you visit `www.google.com`:

- Your browser acts as the **Client**
- Google's computer acts as the **Server**

---

# 🔄 Client-Server Architecture

Most websites follow the **Client-Server Model**.

```
Client (Browser)
       │
       ▼
HTTP Request
       │
       ▼
Server
       │
       ▼
HTTP Response
       │
       ▼
Browser Displays Webpage
```

---

# 📨 What is an HTTP Request?

An **HTTP Request** is a message sent by the browser to the server asking for a webpage or resource.

Example:

```
GET /index.html
```

The browser sends this request when you open a webpage.

---

# 📩 What is an HTTP Response?

An **HTTP Response** is the server's reply to the browser.

The response may include:

- HTML
- CSS
- JavaScript
- Images
- Videos

The browser then displays the webpage.

---

# 🔒 HTTP vs HTTPS

## HTTP

- Stands for HyperText Transfer Protocol
- Data is not encrypted
- Less secure

Example:

```
http://example.com
```

---

## HTTPS

- Stands for HyperText Transfer Protocol Secure
- Data is encrypted
- More secure
- Recommended for all websites

Example:

```
https://example.com
```

---

# 🌍 What is a URL?

A **URL (Uniform Resource Locator)** is the address of a webpage.

Example:

```
https://www.example.com/about
```

Parts of a URL:

- Protocol → https
- Domain Name → www.example.com
- Path → /about

---

# 🌐 What is a Domain Name?

A **Domain Name** is the human-readable name of a website.

Examples:

- google.com
- github.com
- wikipedia.org

Instead of remembering numbers (IP addresses), we use domain names.

---

# 🧮 What is an IP Address?

Every device connected to the Internet has a unique **IP Address**.

Example:

```
142.250.190.78
```

Computers communicate using IP addresses, not domain names.

---

# 🔎 What is DNS?

**DNS (Domain Name System)** converts a domain name into its corresponding IP address.

Example:

```
google.com
        │
        ▼
142.250.xxx.xxx
```

DNS acts like the Internet's phone book.

---

# 🚀 How a Webpage Loads

1. User enters a URL.
2. Browser checks DNS.
3. DNS returns the server's IP address.
4. Browser sends an HTTP request.
5. Server processes the request.
6. Server sends an HTTP response.
7. Browser displays the webpage.

---

# 📌 Summary

By the end of Day 002, you have learned:

- Internet
- World Wide Web
- Browser
- Server
- Client
- HTTP
- HTTPS
- URL
- Domain Name
- IP Address
- DNS
- Client-Server Communication

---

🎉 Congratulations! You have completed **Day 002 – How the Web Works**.