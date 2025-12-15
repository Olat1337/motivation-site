# 💬 Random Quote Flask App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

**Need a spark of inspiration?**
This is a lightweight, styling-ready web application that serves wisdom on demand. It features a clean UI for users and a robust JSON REST API for developers.

![App Preview](https://github.com/Olat1337/motivation-site/blob/edebcc293f8a5037c2d0c20e046c771d6bfcbf02/app_image.png)

---
## ⚡ Features

| Feature | Description |
| :--- | :--- |
| 🎨 **Web Interface** | Minimalist HTML5 & CSS3 design. |
| 🚀 **REST API** | Fast JSON endpoint (`/api/ret_quote`) for external use. |
| 📂 **Flat-File DB** | Zero-config database using a simple `quotes.json`. |
| 🛠 **Hackable** | Easy to customize, extend, and deploy. |

---

## 📂 Project Structure

```text
project_folder/
├── main.py              # 🧠 Application Logic
├── quotes.json          # 📚 Database (JSON)
├── requirements.txt     # 📦 Dependencies
├── static/
│   └── style.css        # 🎨 Styles
└── templates/
    └── home.html        # 🖼️ Frontend View
````

-----

## 🛠️ Installation

Get the code running on your machine in two steps.

### 1\. Clone the Repository

```
git clone https://github.com/Olat1337/motivation-site.git
cd motivation-site
```

### 2\. Install Dependencies

```
pip install -r requirements.txt
```

-----

## 🚀 Usage

Choose your operating system to start the server.

### 🐧 Linux / macOS

```
python3 main.py
```

### 🪟 Windows

```
python main.py
```

-----

## 🔌 API Documentation

Want to use these quotes in your own app? We've got an endpoint for that.

**URL:** `http://127.0.0.1:5000/api/ret_quote`
**Method:** `GET`

**Example Response:**

```json
{
  "author": "Steve Jobs",
  "quote": "The only way to do great work is to love what you do."
}
```

-----

## ⚙️ Customization

Make it yours\! Open `quotes.json` and add your favorite sayings.

```json
[
  {
    "author": "Yoda",
    "quote": "Do, or do not. There is no try."
  }
]
```

-----

## 📄 License

This project is free to use under the [MIT License.