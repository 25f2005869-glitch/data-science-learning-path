# ⚡ Day 062 — Flask Installation and Project Structure

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 062  
**Topic:** Installing Flask and Project Structure

---

## 🐍 Check Python

    python --version

Or:

    python3 --version

---

## 📦 Check pip

    python -m pip --version

---

## 🌱 Create Virtual Environment

    python -m venv .venv

---

## ▶️ Activate

### Windows

    .venv\Scripts\activate

### macOS/Linux

    source .venv/bin/activate

---

## ⏹️ Deactivate

    deactivate

---

## 📥 Install Flask

    python -m pip install flask

---

## 🔎 Verify Flask

    python -c "import flask; print(flask.__version__)"

---

## 📋 Create Requirements File

    python -m pip freeze > requirements.txt

Install dependencies:

    python -m pip install -r requirements.txt

---

## 📁 Project Structure

    flask-project/
    │
    ├── .venv/
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── css/
        ├── js/
        └── images/

---

## 📌 Important Folders

| Folder/File | Purpose |
|---|---|
| `.venv/` | Isolated Python environment |
| `app.py` | Flask application |
| `templates/` | HTML templates |
| `static/` | CSS, JS, images |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Git ignore rules |

---

## 🚀 Minimal `app.py`

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)

---

## ▶️ Run Application

    python app.py

Common local address:

    http://127.0.0.1:5000/

---

## 🧠 Remember

    Flask
      ↓
    app.py
      ↓
    routes
      ↓
    templates + static
      ↓
    browser

---

## ⚠️ Important

- Do not commit `.venv/`
- Do not commit secrets
- Use `requirements.txt`
- Use debug mode only during development
- Keep project structure organized